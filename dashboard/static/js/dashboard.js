
let demandChart;

async function loadDashboard() {
    try {
        const response = await fetch("/api/dashboard-data");
        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Unable to load dashboard");
        }

        // KPI CARDS
        document.getElementById("totalTransactions").textContent =
            data.total_transactions.toLocaleString();

        document.getElementById("productsAnalysed").textContent =
            data.total_products;

        document.getElementById("forecastDemand").textContent =
            data.forecast_total.toLocaleString();

        // TOP PRODUCTS
        document.getElementById("topProducts").innerHTML =
            data.top_products.map((product, index) => `
                <div class="product-row">
                    <span>${index + 1}. ${product.name}</span>
                    <strong>${product.count}</strong>
                </div>
            `).join("");

        // FORECAST TABLE
        document.getElementById("forecastTable").innerHTML =
            data.predictions.map(item => `
                <tr>
                    <td>${item["Item Purchased"]}</td>
                    <td>${Number(item["Predicted Purchase Count"]).toFixed(0)}</td>
                </tr>
            `).join("");

        // INVENTORY INSIGHTS
        const sorted = [...data.predictions].sort(
            (a, b) =>
                Number(b["Predicted Purchase Count"]) -
                Number(a["Predicted Purchase Count"])
        );

        const highThreshold = sorted.length
            ? Number(sorted[Math.floor((sorted.length - 1) * 0.67)]["Predicted Purchase Count"])
            : 0;

        const lowThreshold = sorted.length
            ? Number(sorted[Math.floor((sorted.length - 1) * 0.33)]["Predicted Purchase Count"])
            : 0;

        let high = 0;
        let moderate = 0;
        let low = 0;

        document.getElementById("inventoryTable").innerHTML =
            sorted.map(item => {
                const demand = Number(item["Predicted Purchase Count"]);

                let status;
                let stock;

                if (demand >= highThreshold && demand > 0) {
                    status = "High Demand";
                    stock = Math.ceil(demand * 1.2);
                    high++;
                } else if (demand <= lowThreshold) {
                    status = "Low Demand";
                    stock = Math.ceil(demand * 1.1);
                    low++;
                } else {
                    status = "Moderate Demand";
                    stock = Math.ceil(demand * 1.15);
                    moderate++;
                }

                return `
                    <tr>
                        <td>${item["Item Purchased"]}</td>
                        <td>${demand.toFixed(0)}</td>
                        <td>${stock}</td>
                        <td><span class="demand-status">${status}</span></td>
                    </tr>
                `;
            }).join("");

        document.getElementById("highDemandCount").textContent = high;
        document.getElementById("moderateDemandCount").textContent = moderate;
        document.getElementById("lowDemandCount").textContent = low;

        // MONTHLY DEMAND CHART
        const canvas = document.getElementById("demandChart");

        if (demandChart) {
            demandChart.destroy();
        }

        demandChart = new Chart(canvas, {
            type: "line",
            data: {
                labels: data.monthly_labels,
                datasets: [{
                    label: "Purchase Count",
                    data: data.monthly_values,
                    borderColor: "#18c6b4",
                    backgroundColor: "rgba(24, 198, 180, 0.12)",
                    fill: true,
                    tension: 0.4,
                    pointRadius: 3
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        labels: { color: "#d5e1ee" }
                    }
                },
                scales: {
                    x: {
                        ticks: { color: "#a7b4c5" },
                        grid: { color: "rgba(255,255,255,0.05)" }
                    },
                    y: {
                        beginAtZero: true,
                        ticks: { color: "#a7b4c5" },
                        grid: { color: "rgba(255,255,255,0.05)" }
                    }
                }
            }
        });

    } catch (error) {
        console.error("Dashboard error:", error);

        document.getElementById("topProducts").textContent = error.message;
        document.getElementById("forecastTable").innerHTML =
            `<tr><td colspan="2">${error.message}</td></tr>`;

        document.getElementById("inventoryTable").innerHTML =
            `<tr><td colspan="4">${error.message}</td></tr>`;
    }
}

// SIDEBAR NAVIGATION
const navLinks = document.querySelectorAll(".nav-link");

navLinks.forEach(link => {
    link.addEventListener("click", function () {
        navLinks.forEach(item => item.classList.remove("active"));
        this.classList.add("active");
    });
});

document.addEventListener("DOMContentLoaded", loadDashboard);
