import os
from dotenv import load_dotenv

load_dotenv()

HACKATIME_KEY = os.getenv("HACKATIME_KEY")

# check if key is put in .env
def validate_config():
    if not HACKATIME_KEY:
        raise ValueError("HACKATIME_KEY is missing from .env")
    return True


if __name__ == "__main__":
    validate_config()
    print("Configuration is valid.")