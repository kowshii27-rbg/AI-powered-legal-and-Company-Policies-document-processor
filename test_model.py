import os
from dotenv import load_dotenv
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

# Load environment variables
load_dotenv()

# Configure Google API
GOOGLE_API_KEY = os.getenv("AIzaSyDSDPIWetOug2Gd1O5VwmS3OQXqFNyhYqw")
genai.configure(api_key=GOOGLE_API_KEY)

# Configure safety settings
safety_settings = {
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
}

# Test text generation
model = genai.GenerativeModel('gemini-2.0-pro-exp', safety_settings=safety_settings)

# Create a chat
chat = model.start_chat(history=[])

# Send a message
response = chat.send_message('Write a short poem about AI.')

print("Response:", response.text) 