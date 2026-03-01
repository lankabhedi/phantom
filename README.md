<![CDATA[<div align="center">

# 👻 PHANTOM

### Automated Satellite-Based Infrastructure Audit System

[![License](https://img.shields.io/badge/License-All%20Rights%20Reserved-red.svg)](#license)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![AMD Ryzen AI](https://img.shields.io/badge/AMD-Ryzen%20AI-orange.svg)](https://www.amd.com/en/products/processors/consumer/ryzen-ai.html)

*Bridging the gap between government infrastructure claims and ground reality using satellite imagery and on-device AI.*

</div>

---

## 🔍 The Problem

Government infrastructure projects in remote regions (e.g., PMGSY roads in Meghalaya) are often marked as "complete" in official records — but **do not physically exist**. Manual auditing is slow, expensive, and easily manipulated.

## 💡 The Solution

PHANTOM is an **edge-AI powered audit system** that automatically:
1. **Scrapes** government procurement portals for project claims and GPS coordinates.
2. **Downloads** corresponding Sentinel-2 satellite imagery via the STAC API.
3. **Detects** physical road presence using a U-Net CV model running on the AMD Ryzen AI NPU.
4. **Flags** discrepancies between claims and reality on an interactive evidence dashboard.

---

## 🏗️ Project Structure

```
PHANTOM/
├── scraper/              # PMGSY procurement data scraper (Playwright)
│   └── pmgsy_scraper.py
├── satellite/            # Sentinel-2 imagery downloader (STAC API)
│   └── downloader.py
├── cv/                   # Computer Vision pipeline
│   ├── model.py          # U-Net (ResNet-34) architecture
│   └── inference.py      # On-device inference with spatial masking
├── core/                 # Business logic
│   └── scoring.py        # Discrepancy scoring engine (RED/AMBER/GREEN)
├── web/                  # Interactive audit dashboard
│   ├── index.html        # Leaflet.js dark-themed UI
│   └── app.js            # Map rendering, overlays, and popups
├── data/                 # Generated data artifacts
│   ├── raw_projects.json
│   ├── verified_projects.json
│   └── satellite_images/
├── tests/                # Unit tests
├── requirements.txt      # Python dependencies
└── README.md
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| **AI/ML** | PyTorch, Segmentation Models PyTorch (U-Net + ResNet-34), OpenCV |
| **Geospatial** | Rasterio, PyStac, Rioxarray, Stackstac, Sentinel-2 L2A |
| **Scraping** | Playwright |
| **Dashboard** | Leaflet.js, HTML5, Vanilla JS |
| **Hardware** | AMD Ryzen AI (XDNA NPU) |

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone git@github.com:lankabhedi/phantom.git
cd phantom

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
playwright install

# Run the full pipeline
export PYTHONPATH=$PYTHONPATH:.
python3 cv/inference.py
python3 core/scoring.py

# Launch the dashboard
python3 -m http.server 8000
# Visit http://localhost:8000/web/index.html
```

---

## 📊 Dashboard Features

- **Dark Mode & Satellite Toggle** — Switch between sleek dark tiles and high-res satellite imagery.
- **Ghost Lines** — Dashed white polylines showing the government's *claimed* road path.
- **Built Highlights** — Precision neon-green AI overlay showing what *actually* exists.
- **Discrepancy Tiers** — Projects flagged as 🟢 Verified, 🟡 Uncertain, or 🔴 PHANTOM.

---

## 🎯 AMD Ryzen AI Integration

PHANTOM leverages the AMD Ryzen AI NPU for:
- **Privacy** — Sensitive audit data never leaves the edge device.
- **Offline Capability** — Field auditors in remote areas can run verifications without internet.
- **Efficiency** — Low-power inference on battery for extended fieldwork.

---

## 📜 License

**All Rights Reserved.** See [LICENSE](LICENSE) for details.

This software may not be copied, modified, or distributed without prior written consent.
]]>
