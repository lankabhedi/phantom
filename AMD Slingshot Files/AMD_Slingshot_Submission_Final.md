# PHANTOM: AMD Slingshot Official Submission Content

This content is formatted according to your 12-slide requirement. 

---

## Slide 1 – Team Details
- **Team Name**: PHANTOM
- **Team Leader Name**: [Type Your Name Here]
- **Problem Statement**: Government infrastructure projects, particularly in remote regions like Meghalaya, often suffer from "Ghost Road" syndrome—where projects are marked as complete in records but do not exist in reality. Manual auditing is slow, expensive, and prone to manipulation.

---

## Slide 2 – Brief about the Idea
PHANTOM is an automated, decentralized infrastructure audit system. It uses **Satellite Imagery** and **On-Device Computer Vision (AMD Ryzen AI)** to cross-verify government-claimed road completions (PMGSY records) with physical evidence on the ground. It bridges the gap between digital claims and physical reality.

---

## Slide 3 – Opportunities
- **Existing vs. PHANTOM**: Traditional audits rely on field photos that can be faked or outdated. PHANTOM uses objective, timestamped satellite data and AI verification that cannot be bribed or bypassed.
- **Problem Solving**: It provides an "Analytical Safety Net" for public funds, flagging discrepancies in real-time before final payments are released to contractors.
- **USP**: **"Satellite Evidence as a Service."** It features a unique "Ghost Line" vs. "Built Path" visual comparison that makes audit results understandable for non-technical officials.

---

## Slide 4 – Features
1. **Automated Procurement Scraper**: Live extraction of project IDs, costs, and GPS coordinates from PMGSY portals.
2. **Sentinel-2 STAC Integration**: Automated acquisition of high-resolution, multi-spectral satellite imagery.
3. **On-Device Road Detection**: High-precision U-Net model running on the AMD NPU to identify built infrastructure.
4. **Discrepancy Scoring Engine**: Automated tiering of projects into VERIFIED, UNCERTAIN, or PHANTOM.
5. **Interactive Audit Dashboard**: Geospatial heatmap with satellite overlays and evidence popups.

---

## Slide 5 – Process Flow / Use Case
- **Step 1**: Auditor enters a District/Block in the dashboard.
- **Step 2**: System scrapes latest government claims and downloads recent cloud-free satellite imagery.
- **Step 3**: AMD Ryzen AI NPU processes the imagery to detect road structure.
- **Step 4**: Scorer compares the "AI-Detected path" with the "Claimed path."
- **Step 5**: Results are flagged on the map (Red/Green) with visual evidence for the auditor to review.

---

## Slide 6 – Wireframes / Mockups
- **Dashboard Interface**: Dark-themed, high-resolution Leaflet.js map.
- **Visual Evidence**: Side-by-side comparison.
    - **Left**: Dashed white line over a forest (The Claim).
    - **Right**: Neon green AI highlight (The Physical Reality).
- **Audit Tooltip**: Hovering over a dot reveals the "Road Presence Score" and project metadata.

---

## Slide 7 – Architecture
- **Frontend**: Lightweight HTML5/Leaflet.js dashboard with layer controls.
- **Edge Layer**: Python-based pipeline utilizing **AMD Ryzen AI Software** for model execution.
- **CV Engine**: PyTorch-based U-Net (ResNet-34 backbone) optimized for road semantic segmentation.
- **Data Layer**: Automated STAC API client for imagery and Playwright for procurement records.

---

## Slide 8 – Technologies
- **AI/ML**: PyTorch, Segmentation Models, OpenCV (Road Detection).
- **Geospacial**: Rasterio, PyStac, Rioxarray, Leaflet.js, Sentinel-2 L2A data.
- **Automation**: Playwright (Web Scraping), Python.
- **Hardware Optimization**: AMD Ryzen AI (XDNA architecture).

---

## Slide 9 – Usage of AMD Products/Solutions
- **AMD Ryzen AI (NPU)**: PHANTOM leverages the NPU to run multi-spectral image analysis locally. 
- **Privacy & Security**: Native NPU execution ensures that sensitive government audit data stays on-device and offline.
- **Field-Ready Efficiency**: Low-power inference enables auditors to perform long-duration field inspections on battery power without needing cloud connectivity.

---

## Slide 10 – Estimated Implementation Cost
- **Hardware**: Standard AMD Ryzen AI-powered laptop (Already available to auditor).
- **Imagery**: **$0** (Leverages Earth Search / Sentinel-2 Open Data).
- **Software**: **$0** (Built using open-source Python stacks and Leaflet).
- **Maintenance**: Extremely low due to serverless/decentralized architecture.

---

## Slide 11 – Prototype Assets
- **GitHub Public Repository**: [Link to your PHANTOM Repo]
- **Demo Video**: [Link to your 3-Minute Demo]
- **Sample Evidence**: Interactive dashboard hosted locally showing a verified "Phantom Road" in Meghalaya.

---

## Slide 12 – Additional Requirements
- **Future Expansion**: Scaleable to monitor Bridges, Dams, and public buildings using the same geospatial comparison logic.
- **Societal Impact**: Direct alignment with the United Nations Sustainable Development Goal (SDG) 16: Peace, Justice, and **Strong Institutions**.
- **Transparency**: Open-data approach allows citizens to verify their own local projects.
