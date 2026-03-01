import json
import os

def compute_discrepancy(projects_data, cv_scores):
    """
    Compares government claims with CV scores and assigns a discrepancy tier.
    
    Tiers:
    - GREEN: Verified (Gov Claims Complete, CV Score > 0.6)
    - AMBER: Uncertain (CV Score between 0.3 and 0.6)
    - RED: PHANTOM (Gov Claims Complete, CV Score < 0.3)
    """
    verified_projects = []
    
    for project in projects_data:
        p_id = project["id"]
        cv_score = cv_scores.get(p_id, 0)
        
        # In PHANTOM, status typically 1 means "Complete"
        # For simplicity, we assume status is "Complete" for these projects
        
        if cv_score < 0.3:
            tier = "RED"
            label = "PHANTOM"
        elif cv_score < 0.6:
            tier = "AMBER"
            label = "UNCERTAIN"
        else:
            tier = "GREEN"
            label = "VERIFIED"
            
        # Try to load bbox if exists
        bbox = None
        bbox_file = os.path.join("/home/samnitmehandiratta/Documents/PHANTOM/data/satellite_images", f"{p_id}_mask_bbox.json")
        if os.path.exists(bbox_file):
            with open(bbox_file, "r") as f:
                bbox = json.load(f)

        verified_projects.append({
            **project,
            "cv_score": cv_score,
            "tier": tier,
            "label": label,
            "bbox": bbox,
            "discrepancy": abs(1.0 - cv_score) if label == "PHANTOM" else 0
        })
        
    return verified_projects

if __name__ == "__main__":
    # Mock some CV scores for demonstration if we have multiple projects
    # For now, we take results from our inference script
    
    data_dir = "/home/samnitmehandiratta/Documents/PHANTOM/data"
    raw_file = os.path.join(data_dir, "raw_projects.json")
    out_file = os.path.join(data_dir, "verified_projects.json")
    
    if os.path.exists(raw_file):
        with open(raw_file, "r") as f:
            raw_data = json.load(f)
            
        # Example CV score from our inference (assuming it's around 0.1 for a phantom project)
        # In a real pipeline, we'd pull this from a database or intermediate file
        cv_scores = {
            "MG01III028": 0.15 # Example: Flagging our verified project as phantom for demonstration
        }
        
        verified_data = compute_discrepancy(raw_data, cv_scores)
        
        with open(out_file, "w") as f:
            json.dump(verified_data, f, indent=4)
            
        print(f"Saved verified projects to {out_file}")
    else:
        print(f"Raw data not found at {raw_file}")
