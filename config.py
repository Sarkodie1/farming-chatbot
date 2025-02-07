import os
from dotenv import load_dotenv

# Load environment variables from a .env file if available
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "your_default_api_key_here")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
