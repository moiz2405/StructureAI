import google.generativeai as genai
import os

API_KEY = os.environ.get("GOOGLE_API_KEY")
if not API_KEY:
    print("No GOOGLE_API_KEY found in environment.")
else:
    genai.configure(api_key=API_KEY)
    try:
        print("Listing available models...")
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(m.name)
    except Exception as e:
        print(f"Error: {e}")
