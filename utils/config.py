import os
from dotenv import load_dotenv

# Load .env from utils folder
_env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(_env_path)

USAJOBS_API_KEY = os.getenv("USAJOBS_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
