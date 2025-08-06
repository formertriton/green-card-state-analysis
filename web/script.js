// Configuration
const width = 960;
const height = 500;
const API_BASE = 'http://127.0.0.1:5000/api';

// Create SVG
const svg = d3.select("#map")
    .attr("viewBox", `0 0 ${width} ${height}`)
    .attr("width", "100%")
    .attr("height", "100%");

const tooltip = d3.select("#tooltip");

// US map projection
const projection = d3.geoAlbersUsa()
    .scale(1000)
    .translate([width / 2, height / 2]);

const path = d3.geoPath().projection(projection);

// State ID to name mapping (simplified for common states)
const stateIdToName = {
    1: "Alabama", 2: "Alaska", 4: "Arizona", 5: "Arkansas", 6: "California",
    8: "Colorado", 9: "Connecticut", 10: "Delaware", 12: "Florida", 13: "Georgia",
    15: "Hawaii", 16: "Idaho", 17: "Illinois", 18: "Indiana", 19: "Iowa",
    20: "Kansas", 21: "Kentucky", 22: "Louisiana", 23: "Maine", 24: "Maryland",
    25: "Massachusetts", 26: "Michigan", 27: "Minnesota", 28: "Mississippi", 29: "Missouri",
    30: "Montana", 31: "Nebraska", 32: "Nevada", 33: "New Hampshire", 34: "New Jersey",
    35: "New Mexico", 36: "New York", 37: "North Carolina", 38: "North Dakota", 39: "Ohio",
    40: "Oklahoma", 41: "Oregon", 42: "Pennsylvania", 44: "Rhode Island", 45: "South Carolina",
    46: "South Dakota", 47: "Tennessee", 49: "Utah", 50: "Vermont", 51: "Virginia",
    53: "Washington", 54: "West Virginia", 55: "Wisconsin", 56: "Wyoming", 11: "District of Columbia"
};

// Load US states data and create map
const usStatesUrl = "https://cdn.jsdelivr.net/npm/us-atlas@3/states-10m.json";

d3.json(usStatesUrl).then(function(us) {
    const states = topojson.feature(us, us.objects.states);
    
    svg.selectAll(".state")
        .data(states.features)
        .enter()
        .append("path")
        .attr("class", "state")
        .attr("d", path)
        .on("mouseover", handleStateHover)
        .on("mousemove", handleMouseMove)
        .on("mouseout", handleMouseOut);
});

// Event handlers
function handleStateHover(event, d) {
    const stateName = stateIdToName[d.id];
    
    if (stateName) {
        // Fetch data from your API
        fetch(`${API_BASE}/state/${encodeURIComponent(stateName)}`)
            .then(response => response.json())
            .then(data => {
                showTooltip(data);
                updateStatsPanel(data);
            })
            .catch(error => {
                console.error('Error fetching state data:', error);
                showErrorTooltip(stateName);
            });
    }
}

function handleMouseMove(event) {
    tooltip
        .style("left", (event.pageX + 10) + "px")
        .style("top", (event.pageY - 10) + "px");
}

function handleMouseOut() {
    tooltip.style("opacity", 0);
}

function showTooltip(data) {
    const countriesHtml = data.top_countries.map(country => 
        `<div class="country-item">
            <span>${country.Country}</span>
            <span>${country.total.toLocaleString()}</span>
        </div>`
    ).join('');

    tooltip.style("opacity", 1)
        .html(`
            <h3>${data.state}</h3>
            <div class="total">Total: ${data.total_admissions.toLocaleString()}</div>
            <div><strong>Top 3 Countries:</strong></div>
            ${countriesHtml}
        `);
}

function showErrorTooltip(stateName) {
    tooltip.style("opacity", 1)
        .html(`
            <h3>${stateName}</h3>
            <p>No data available</p>
        `);
}

function updateStatsPanel(data) {
    const statsPanel = d3.select("#stats");
    
    statsPanel.html(`
        <div class="stat-card">
            <h3>${data.state}</h3>
            <p>Selected State</p>
        </div>
        <div class="stat-card">
            <h3>${data.total_admissions.toLocaleString()}</h3>
            <p>Total Green Cards (2018-2022)</p>
        </div>
        <div class="stat-card">
            <h3>${data.top_countries[0].Country}</h3>
            <p>Top Country (${data.top_countries[0].total.toLocaleString()})</p>
        </div>
    `);
}

// Initialize
console.log("Green Card Map initialized. Hover over states to see data!");