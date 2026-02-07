function getDecision() {
    const moistureInput = document.getElementById("moisture").value.trim();
    const moisture = Number(moistureInput);

    let decision = "";
    let reason = "";
    let cssClass = "";

    // Safety check
    if (isNaN(moisture)) {
        alert("Please enter a valid soil moisture value");
        return;
    }

    if (moisture > 60) {
        decision = "❌ REFUSE IRRIGATION";
        reason = "Soil moisture is already sufficient.";
        cssClass = "refuse";
    } 
    else if (moisture >= 41 && moisture <= 60) {
        decision = "⚠️ LIMITED IRRIGATION";
        reason = "Moderate moisture detected. Controlled watering advised.";
        cssClass = "limited";
    } 
    else {
        decision = "✅ ALLOW IRRIGATION";
        reason = "Low soil moisture. Irrigation recommended.";
        cssClass = "allow";
    }

    document.getElementById("resultBox").classList.remove("hidden");
    document.getElementById("decisionText").innerText = decision;
    document.getElementById("decisionText").className = cssClass;
    document.getElementById("reasonText").innerText = reason;
}
