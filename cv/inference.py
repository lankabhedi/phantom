import torch
import numpy as np
import rasterio
import os
import json
from cv.model import get_unet_model
import cv2

def run_inference(image_path, model, output_mask_path, start_coords=None, end_coords=None):
    print(f"Running inference on {image_path}...")
    
    with rasterio.open(image_path) as src:
        # Read RGB bands
        image = src.read([1, 2, 3]) # (C, H, W)
        transform = src.transform
        height, width = src.height, src.width
        # Normalize
        image = image.astype(np.float32) / 255.0
        
    input_tensor = torch.from_numpy(image).unsqueeze(0) # (1, C, H, W)
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    input_tensor = input_tensor.to(device)
    
    with torch.no_grad():
        output = model(input_tensor)
        probs = torch.sigmoid(output).squeeze().cpu().numpy()
        
    # --- Refinement: Spatial Masking ---
    if start_coords and end_coords:
        # Create a spatial buffer mask
        spatial_mask = np.zeros((height, width), dtype=np.uint8)
        
        # Transform GPS to Pixel
        # rasterio rowcol returns (row, col)
        start_px = src.index(start_coords[1], start_coords[0]) # (lon, lat)
        end_px = src.index(end_coords[1], end_coords[0])
        
        # Draw a thick line (buffer) between start and end
        # cv2.line uses (x, y) which is (col, row)
        cv2.line(spatial_mask, (start_px[1], start_px[0]), (end_px[1], end_px[0]), 1, thickness=20)
        
        # Apply mask to probabilities
        probs = probs * spatial_mask

    # --- Refinement: Higher Threshold ---
    # High probability means road detected
    # Create an RGBA image
    h, w = probs.shape
    rgba = np.zeros((h, w, 4), dtype=np.uint8)
    
    road_pixels = probs > 0.6 # Increased threshold (was 0.5)
    
    # Set RGB to Neon Green (57, 255, 20)
    rgba[road_pixels, 0] = 57
    rgba[road_pixels, 1] = 255
    rgba[road_pixels, 2] = 20
    # Set Alpha based on probability
    rgba[road_pixels, 3] = 200 # Semi-transparent
    
    # Save mask as PNG
    cv2.imwrite(output_mask_path, cv2.cvtColor(rgba, cv2.COLOR_RGBA2BGRA))
    print(f"Saved refined road mask to {output_mask_path}")
    
    # Get bounding box for image overlay in Leaflet
    bbox = [src.bounds.bottom, src.bounds.left, src.bounds.top, src.bounds.right]
    
    # Compute a simple presence score
    score = np.mean(probs)
    return score, bbox

if __name__ == "__main__":
    model = get_unet_model()
    model.eval()
    
    # Load project data to get start/end coords
    data_path = "/home/samnitmehandiratta/Documents/PHANTOM/data/raw_projects.json"
    p_id = "MG01III028"
    
    start_c, end_c = None, None
    if os.path.exists(data_path):
        with open(data_path, "r") as f:
            projects = json.load(f)
            for p in projects:
                if p["id"] == p_id:
                    start_c = (p["start_lat"], p["start_lon"])
                    end_c = (p["end_lat"], p["end_lon"])
                    break

    img_path = f"/home/samnitmehandiratta/Documents/PHANTOM/data/satellite_images/{p_id}_current.tif"
    mask_path = f"/home/samnitmehandiratta/Documents/PHANTOM/data/satellite_images/{p_id}_mask.png"
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(mask_path), exist_ok=True)
    
    if os.path.exists(img_path):
        score, bbox = run_inference(img_path, model, mask_path, start_c, end_c)
        print(f"Road Presence Score: {score:.4f}")
        print(f"BBox: {bbox}")
        
        # Save bbox to a side file for the UI
        with open(mask_path.replace(".png", "_bbox.json"), "w") as f:
            json.dump(bbox, f)
    else:
        print(f"Image not found at {img_path}")
