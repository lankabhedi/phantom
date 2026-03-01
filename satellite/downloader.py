import json
import os
from pystac_client import Client
import stackstac
import xarray as xr
import rioxarray

def download_sentinel_image(lat, lon, date_range, output_path):
    """
    Downloads a Sentinel-2 image for a given area and date range using STAC.
    """
    print(f"Searching for imagery at {lat}, {lon} for {date_range}...")
    
    catalog = Client.open("https://earth-search.aws.element84.com/v1")
    
    # Define a small bounding box around the point
    buffer = 0.01 # Approx 1km
    bbox = [lon - buffer, lat - buffer, lon + buffer, lat + buffer]
    
    search = catalog.search(
        collections=["sentinel-2-l2a"],
        bbox=bbox,
        datetime=date_range,
        query={"eo:cloud_cover": {"lt": 20}}, # Less than 20% cloud cover
        sortby=[{"field": "properties.eo:cloud_cover", "direction": "asc"}]
    )
    
    items = search.get_all_items()
    if not items:
        print("No items found.")
        return False
    
    # Pick the best item (least cloud cover)
    item = items[0]
    print(f"Found item: {item.id} with cloud cover {item.properties['eo:cloud_cover']}%")
    
    # Use stackstac to load the data with a specified CRS
    bands = ["red", "green", "blue"]
    data = stackstac.stack(item, assets=bands, bounds_latlon=bbox, epsg=4326)
    
    # Compute the median or just take the first time step if multiple
    # and scale to 8-bit for visualization
    rgb = data.squeeze().compute()
    
    # Normalize and save as GeoTIFF or PNG
    # For now, let's save as GeoTIFF using rioxarray
    rgb.rio.to_raster(output_path)
    print(f"Saved image to {output_path}")
    return True

if __name__ == "__main__":
    # Example using coordinate from scraper
    example_lat = 25.8852434
    example_lon = 90.8718331
    example_date = "2024-01-01/2024-12-31"
    
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    os.makedirs(os.path.join(project_root, "data/satellite_images"), exist_ok=True)
    out_file = os.path.join(project_root, "data/satellite_images/MG01III028_current.tif")
    
    download_sentinel_image(example_lat, example_lon, example_date, out_file)
