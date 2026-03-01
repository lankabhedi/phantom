<![CDATA[<div align="center">

<img src="https://img.shields.io/badge/👻-PHANTOM-000000?style=for-the-badge&labelColor=000000&color=39FF14" alt="PHANTOM" />

<br/>

# PHANTOM

**Satellite-Powered Ghost Infrastructure Detection**

<br/>

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-U--Net-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)](https://pytorch.org)
[![AMD Ryzen AI](https://img.shields.io/badge/AMD-Ryzen%20AI%20NPU-ED1C24?style=flat-square&logo=amd&logoColor=white)](https://www.amd.com)
[![Sentinel-2](https://img.shields.io/badge/ESA-Sentinel--2-003399?style=flat-square&logo=data:image/svg+xml;base64,&logoColor=white)](https://sentinel.esa.int)
[![License](https://img.shields.io/badge/license-All%20Rights%20Reserved-red?style=flat-square)](LICENSE)

<br/>

*Every year, billions in public infrastructure funds vanish into projects that exist only on paper.*
*PHANTOM finds them.*

<br/>

---

</div>

<br/>

## The Problem

India's **PMGSY** (Pradhan Mantri Gram Sadak Yojana) has sanctioned over **₹2.7 lakh crore** for rural roads. In remote states like Meghalaya, some roads are marked **"100% complete"** in government databases — but **don't physically exist**.

Traditional audits require inspectors to travel to dangerous, inaccessible terrain. They're slow, expensive, and easily falsified with staged photographs.

**There is no scalable way to verify if a road was actually built.**

<br/>

## How PHANTOM Works

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐     ┌──────────────────┐
│  📋 SCRAPER     │────▶│  🛰️ SATELLITE    │────▶│  🧠 CV ENGINE   │────▶│  🗺️ DASHBOARD   │
│                 │     │                  │     │                 │     │                  │
│ PMGSY Portal    │     │ Sentinel-2 STAC  │     │ U-Net + AMD NPU │     │ Leaflet.js Map   │
│ Project Claims  │     │ Multi-spectral   │     │ Road Detection  │     │ Evidence Overlay  │
│ GPS Coordinates │     │ Cloud-free Tiles │     │ Spatial Masking │     │ Discrepancy Tiers│
└─────────────────┘     └──────────────────┘     └─────────────────┘     └──────────────────┘
```

<br/>

### The Audit Trail

| What You See | What It Means |
|:---:|:---|
| ⚪ **Dashed White Line** | The road the government *claims* was built ("Ghost Line") |
| 🟢 **Neon Green Overlay** | The road the AI *actually detected* from satellite imagery |
| 🔴 **Red Marker** | PHANTOM Project — claim exists, road does not |
| 🟡 **Amber Marker** | Uncertain — partial construction or low confidence |
| 🟢 **Green Marker** | Verified — road matches the claim |

<br/>

## Why AMD Ryzen AI

PHANTOM doesn't use the cloud. It runs **entirely on-device**.

| | Cloud-Based Audit | PHANTOM (Edge AI) |
|---|:---:|:---:|
| **Privacy** | Audit data on third-party servers | Never leaves your laptop |
| **Connectivity** | Requires high-speed internet | Works offline in the field |
| **Cost** | GPU compute bills per inference | $0 after hardware |
| **Latency** | Minutes per tile (queue + upload) | Seconds per tile (NPU) |

The AMD Ryzen AI **XDNA NPU** handles the heavy semantic segmentation workload while keeping power consumption low enough for battery-powered fieldwork in remote Meghalaya.

<br/>

## Project Structure

```
PHANTOM/
│
├── scraper/
│   └── pmgsy_scraper.py        # Playwright-based procurement scraper
│
├── satellite/
│   └── downloader.py           # STAC API → Sentinel-2 imagery
│
├── cv/
│   ├── model.py                # U-Net (ResNet-34 encoder)
│   └── inference.py            # Spatial-masked road detection
│
├── core/
│   └── scoring.py              # RED / AMBER / GREEN classification
│
├── web/
│   ├── index.html              # Dark-themed dashboard UI
│   └── app.js                  # Map layers, overlays, popups
│
├── data/
│   ├── raw_projects.json       # Scraped project metadata
│   ├── verified_projects.json  # Scored audit results
│   └── satellite_images/       # GeoTIFFs and detection masks
│
├── requirements.txt
├── LICENSE
└── README.md
```

<br/>

## Quick Start

```bash
git clone git@github.com:lankabhedi/phantom.git
cd phantom

python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
playwright install

# Run the audit pipeline
export PYTHONPATH=$PYTHONPATH:.
python3 cv/inference.py       # Detect roads in satellite imagery
python3 core/scoring.py       # Score and classify discrepancies

# Launch dashboard
python3 -m http.server 8000
# → http://localhost:8000/web/index.html
```

<br/>

## Tech Stack

| Layer | Tools |
|---|---|
| **Computer Vision** | PyTorch · Segmentation Models PyTorch · OpenCV |
| **Geospatial** | Rasterio · PyStac · Rioxarray · Stackstac · Sentinel-2 L2A |
| **Scraping** | Playwright (Headless Chromium) |
| **Frontend** | Leaflet.js · Vanilla JS · HTML5 |
| **Hardware** | AMD Ryzen AI · XDNA NPU |

<br/>

## Hackathon

Built for **AMD Slingshot** under the themes:
- 🌍 **AI for Social Good** — Accountability for public infrastructure
- 🚀 **Open Innovation** — Edge-first AI on consumer hardware

<br/>

---

<div align="center">

**PHANTOM** · Built with 🔥 for AMD Slingshot

*All Rights Reserved · See [LICENSE](LICENSE)*

</div>
]]>
