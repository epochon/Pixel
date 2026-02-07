class CropAgent:
    def analyze(self, context):
        crop = context["crop"]

        # Simple crop-based logic
        if crop.lower() in ["rice", "sugarcane"]:
            return {"crop": "ALLOW", "reason": "Crop requires high water"}
        else:
            return {"crop": "CONDITIONAL", "reason": "Crop requires moderate water"}