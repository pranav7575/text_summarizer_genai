from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Validate required environment variables
def validate_env_vars():
    if not GOOGLE_API_KEY:
        raise ValueError("GOOGLE_API_KEY is not set in .env file")

# Call this function when your application starts
validate_env_vars()