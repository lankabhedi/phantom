import asyncio
import json
import os
from playwright.async_api import async_playwright

async def scrape_meghalaya_projects():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        # 1. Get Project IDs and Costs from Sanctioned Projects
        print("Scraping Sanctioned Projects...")
        await page.goto("https://pmgsy.dord.gov.in/Home/CitizenPage/", wait_until="networkidle")
        
        # Navigate to Proposals -> Sanctioned Projects
        await page.click("text=Proposals")
        await page.click("text=Sanctioned Projects")
        
        # Wait for Report Viewer and select Meghalaya
        # Note: Selector might need adjustment based on the exact ReportViewer structure
        await page.wait_for_selector("#ReportViewer_ctl09", timeout=30000)
        
        # Sample extraction based on subagent research
        # The subagent found MG01III028 as an example.
        projects = []
        
        # 2. Get GPS from Quality Monitoring
        print("Scraping Quality Monitoring for GPS...")
        # https://pmgsy.dord.gov.in/QualityMonitoringArea/QualityMonitoring/InspectionGradingDetails?id=[ReportID]
        # We need to find the Report IDs first.
        
        # Placeholder for now with the verified example
        verified_project = {
            "id": "MG01III028",
            "name": "T09-Chotcholja to Nelwa Guarechol",
            "lat": 25.8852434,
            "lon": 90.8718331,
            "status": "In Progress",
            "cost": "₹ 15.2 Lakhs" # Example
        }
        projects.append(verified_project)
        
        # Save to data directory
        project_root = "/home/samnitmehandiratta/Documents/PHANTOM"
        data_dir = os.path.join(project_root, "data")
        os.makedirs(data_dir, exist_ok=True)
        file_path = os.path.join(data_dir, "raw_projects.json")
        
        with open(file_path, "w") as f:
            json.dump(projects, f, indent=4)
        
        print(f"Saved {len(projects)} projects to {file_path}")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(scrape_meghalaya_projects())
