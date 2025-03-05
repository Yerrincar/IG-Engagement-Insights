import os
from dotenv import load_dotenv

load_dotenv(".env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "Gemini 1.5 flash"
TEMPERATURE = 0.0