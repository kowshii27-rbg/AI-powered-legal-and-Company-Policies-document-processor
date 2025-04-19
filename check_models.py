import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google API
GOOGLE_API_KEY = os.getenv("AIzaSyDSDPIWetOug2Gd1O5VwmS3OQXqFNyhYqw")
genai.configure(api_key=GOOGLE_API_KEY)

# List available models
print("Available Models:")
for model in genai.list_models():
    print(f"Name: {model.name}")
    print(f"Display name: {model.display_name}")
    print(f"Description: {model.description}")
    print(f"Generation methods: {model.supported_generation_methods}")
    print("---") 