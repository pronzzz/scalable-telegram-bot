import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """
    Configuration class to hold environment variables and constants.
    Using a class allows for easier testing and mocking.
    """
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
    
    # Validation
    if not TELEGRAM_BOT_TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN is not set in environment variables.")

    @property
    def is_production(self):
        return self.ENVIRONMENT.lower() == "production"

config = Config()
