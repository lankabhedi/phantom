## Slide 1 – Team Details

- **Team name** – PHANTOM
- **Team leader name** – [Type your name]
- **Problem Statement** – Government infrastructure funds intended for remote regions are often siphoned into "ghost projects" (claimed as complete but physically non-existent), while manual auditing remains too slow, dangerous, and expensive to verify ground reality.

---

## Slide 2 – Brief about the Idea

**Brief about the idea**
PHANTOM is an automated, edge-device infrastructure audit system. It scrapes government procurement data (e.g., PMGSY) and downloads the corresponding Sentinel-2 satellite imagery for the claimed GPS coordinates. It then uses an on-device Computer Vision model (running on an AMD Ryzen AI NPU) to detect whether the physical road matches the claimed coordinates, automatically flagging discrepancies or "phantom" projects.

---

## Slide 3 – Opportunities

**Opportunities**
PHANTOM provides a scalable, bias-free "Analytical Safety Net" for public funds, enabling governments, NGOs, and citizens to independently verify infrastructure completion from anywhere without physical field visits.

**How different is it from any of the other existing ideas?**
Current audits rely on manual field inspections or geo-tagging photos on mobile apps, which are often faked, outdated, or delayed. PHANTOM relies on objective, timestamped satellite data and automated AI verification that cannot be manipulated on the ground.

**How will it be able to solve the problem?**
By automating the cross-referencing between financial claims (ghost lines) and physical satellite reality (built paths), PHANTOM proactively catches false claims before final payments are released, ensuring accountability.

**USP of the proposed solution**
"Satellite Evidence as a Service"—a decentralized, privacy-first auditing platform that runs entirely on a local AMD NPU, requiring no expensive cloud computing to verify large-scale geographic data.

---

## Slide 4 – Features

**List of features offered by the solution**
- **Automated Procurement Scraper**: Live extraction of project IDs, costs, and geographic claims (Start/End coordinates).
- **Automated Satellite Sync**: STAC API integration to download recent Sentinel-2 multi-spectral imagery.
- **On-Device Road Detection**: PyTorch U-Net model with spatial buffering, optimized for edge execution.
- **Discrepancy Scoring Engine**: Algorithmic flagging of projects as "VERIFIED," "UNCERTAIN," or "PHANTOM" (RED/AMBER/GREEN).
- **Interactive Visual Evidence Dashboard**: Geo-spatial Leaflet map displaying the "Claimed Path" (dashed white line) against the "Built Path" (AI-detected neon green overlay).

---

## Slide 5 – Process Flow / Use Case

**Process flow diagram or Use-case diagram**
1. **Data Ingestion**: System scrapes latest government claims from procurement portals.
2. **Imagery Acquisition**: Downloader automatically fetches recent, cloud-free Sentinel-2 satellite imagery of the region.
3. **Edge Inference**: AMD Ryzen AI NPU runs the Computer Vision model locally to isolate and mask built roads within the claimed area.
4. **Scoring Match**: Algorithm compares the physical AI-detected road mask against the claimed GPS coordinates to compute a discrepancy score.
5. **Dashboarding**: Interactive map displays the audited project outcome with visual geographic evidence overlays.

---

## Slide 6 – Wireframes / Mockups (Optional)

**Wireframes/Mock diagrams of the proposed solution (optional)**
*[Insert screenshot of the PHANTOM Interactive Dashboard with a RED marker clicked, showing the pop-up of the discrepancy and satellite toggles]*

---

## Slide 7 – Architecture

**Architecture diagram of the proposed solution**
- **Data Ingestion Layer**: Python (Playwright, PyStac, Stackstac) -> Extracts claims and resolves Earth Observation data.
- **Edge Compute Layer**: PyTorch + AMD Ryzen AI Software -> Hardware-accelerated semantic segmentation on local NPU.
- **Business Logic Layer**: Python (Core Scoring Engine) -> Calculates spatial discrepancy metrics and mapping bounds.
- **Presentation Layer**: HTML/JS (Leaflet.js) -> Renders the interactive geospatial evidence dashboard.

---

## Slide 8 – Technologies

**Technologies to be used in the solution**
- **AI/ML Models**: PyTorch, Segmentation Models PyTorch (U-Net with ResNet-34 backbone), OpenCV.
- **Geospatial Analysis**: Rasterio, PyStac, Rioxarray, Stackstac, Sentinel-2 L2A satellite data.
- **Web & Automation**: Playwright for dynamic scraping, Leaflet.js for interactive mapping.
- **Hardware Target**: AMD Ryzen AI (XDNA architecture).

---

## Slide 9 – Usage of AMD Products/Solutions

**Usage of AMD Products/Solutions**
The PHANTOM pipeline natively leverages the AMD Ryzen AI NPU to perform the computationally heavy semantic segmentation of large multi-spectral satellite tiles directly on the auditor's laptop. This provides three major benefits:
1. **Low Latency**: Processes large-scale imaging locally without streaming gigabytes of data to a cloud server.
2. **Privacy & Security**: Sensitive government audit locations and the resulting investigations never leave the edge device.
3. **Offline Auditing**: Enables field auditors in remote locations (like Meghalaya) to run AI verifications on laptop battery power without internet connectivity.

---

## Slide 10 – Estimated Implementation Cost (Optional)

**Estimated implementation cost (optional)**
- **Hardware**: Standard AMD Ryzen AI-powered laptop (Pre-existing asset/Sunk cost for auditors).
- **Satellite Imagery**: $0 (Leverages free Earth Search / Sentinel-2 Open Data API).
- **Software/Infrastructure**: $0 (Built entirely using open-source Python libraries with no recurring cloud compute or VM subscription costs thanks to local inference).
- **Overall**: Highly scalable at near-zero marginal cost.

---

## Slide 11 – Prototype Assets

**Prototype Assets (Optional)**
- **GitHub Public Repository Link**: [Insert Link to your repo]
- **Demo Video Link (Max: 3 Minutes)**: [Insert Link to your video]

---

## Slide 12 – Additional Requirements

**Type here**
- **Alignment with Hackathon Theme**: Fits perfectly under "Open Innovation" and "AI for Social Good," providing a novel edge-AI approach to social accountability and reducing infrastructure waste.
- **Scalability & Impact**: The architecture is universally applicable and can be expanded from analyzing rural roads to verifying bridges, dams, and municipal buildings globally.

**Add as per the requirements of the contest**
*[Leave blank or add any other specific references required by the portal]*
