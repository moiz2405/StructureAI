import os
import json
import google.generativeai as genai
from PIL import Image
import io
from schemas import AnalysisResponse

# Configure API Key (User should set this env var or replace it)
# For now, we'll try to get it from os.environ, or let the user know.
API_KEY = os.environ.get("GOOGLE_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)

def analyze_image(image_bytes: bytes) -> AnalysisResponse:
    if not API_KEY:
        # Return a mock response if no key is present, for UI testing
        return AnalysisResponse(
            damage_score=0,
            safety_rating="Unknown (No API Key)",
            identified_issues=[{"issue": "API Key missing", "severity": "Critical"}],
            maintenance_suggestions=["Please set GOOGLE_API_KEY environment variable"],
            inspection_summary="System is not configured with an API key. Please provide a Google Gemini API Key."
        )

    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        
        image = Image.open(io.BytesIO(image_bytes))

        prompt = """
        Analyze this image for structural damage (cracks, corrosion, wear, etc.).
        Provide a detailed assessment in the following JSON format:
        {
            "damage_score": (integer 0-10, where 0 is perfect and 10 is critical failure),
            "safety_rating": "Safe" | "Caution" | "Danger",
            "identified_issues": [
                {"issue": "description of issue", "severity": "Low"|"Medium"|"High", "location": "approximate location"}
            ],
            "maintenance_suggestions": ["list", "of", "actionable", "steps"],
            "inspection_summary": "A professional summary of the inspection findings."
        }
        Return ONLY the JSON.
        """

        response = model.generate_content([prompt, image])
        
        # Clean up response text to ensure it's valid JSON
        text = response.text.strip()
        if text.startswith("```json"):
            text = text[7:-3]
        elif text.startswith("```"):
            text = text[3:-3]
        
        data = json.loads(text)
        return AnalysisResponse(**data)

    except Exception as e:
        print(f"Error analyzing image: {e}")
        return AnalysisResponse(
            damage_score=-1,
            safety_rating="Error",
            identified_issues=[{"issue": str(e), "severity": "Error"}],
            maintenance_suggestions=["Check logs for details"],
            inspection_summary="An error occurred during analysis."
        )
