const map = L.map('map').setView([25.5, 91.5], 8); // Centered on Meghalaya

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

const dark = L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
    attribution: '© OpenStreetMap © CARTO'
}).addTo(map);

const satellite = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
    attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EBP, and the GIS User Community'
});

const baseMaps = {
    "Sleek Dark": dark,
    "Satellite": satellite
};

L.control.layers(baseMaps).addTo(map);

async function loadProjects() {
    try {
        const response = await fetch('../data/verified_projects.json');
        const projects = await response.json();

        let phantomCount = 0;
        document.getElementById('stat-total').innerText = projects.length;

        projects.forEach(project => {
            const color = project.tier === 'RED' ? '#ff7675' :
                project.tier === 'AMBER' ? '#fdcb6e' : '#55efc4';

            if (project.tier === 'RED') phantomCount++;

            // 1. Suggested Road (Dashed Polyline)
            if (project.start_lat && project.end_lat) {
                const polyline = L.polyline([
                    [project.start_lat, project.start_lon],
                    [project.end_lat, project.end_lon]
                ], {
                    color: 'white',
                    dashArray: '5, 10',
                    weight: 2,
                    opacity: 0.6
                }).addTo(map);
                polyline.bindTooltip("Suggested Road (Claimed)", { sticky: true });
            }

            // 2. Built Road Highlight (CV Mask Overlay)
            if (project.bbox) {
                const imageBounds = [
                    [project.bbox[0], project.bbox[1]], // bottom, left
                    [project.bbox[2], project.bbox[3]]  // top, right
                ];
                L.imageOverlay(`../data/satellite_images/${project.id}_mask.png`, imageBounds, {
                    opacity: 0.8,
                    interactive: true
                }).addTo(map).bindTooltip("Built Road (CV Detected)", { sticky: true });
            }

            const marker = L.circleMarker([project.lat, project.lon], {
                radius: 8,
                fillColor: color,
                color: "#fff",
                weight: 1,
                opacity: 1,
                fillOpacity: 0.8
            }).addTo(map);

            const popupContent = `
                <div class="project-popup">
                    <h3>${project.name}</h3>
                    <p><b>ID:</b> ${project.id}</p>
                    <p><b>Status:</b> ${project.status}</p>
                    <p><b>CV Road Score:</b> ${(project.cv_score * 100).toFixed(1)}%</p>
                    <p><b>Tier:</b> <span style="color: ${color}; font-weight: bold;">${project.label}</span></p>
                    <p><b>Satellite View:</b></p>
                    <img src="../data/satellite_images/${project.id}_mask.png" alt="Road Detection Mask" onerror="this.src='https://via.placeholder.com/300x200?text=Mask+Not+Available'">
                </div>
            `;
            marker.bindPopup(popupContent);
        });

        document.getElementById('stat-phantom').innerText = phantomCount;
    } catch (error) {
        console.error("Error loading projects:", error);
    }
}

loadProjects();
