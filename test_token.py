import os
from dotenv import load_dotenv
import replicate

# Load environment variables
load_dotenv()

# Get API token
api_token = os.getenv("REPLICATE_API_TOKEN")
print(f"API Token found: {'Yes' if api_token else 'No'}")

try:
    # List available models
    client = replicate.Client(api_token=api_token)
    models = client.models.list()
    print("\nAvailable models:")
    for model in models:
        print(f"- {model.owner}/{model.name}")
except Exception as e:
    print(f"\nError: {str(e)}") 