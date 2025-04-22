from dotenv import load_dotenv
import os
from pathlib import Path
from .exceptions.exceptions import App_ai_Exception
from .logger.logger import ai_agent_logger as sage_logger

# Load environment variables
load_dotenv()


class Config:
    """Application Configuration Class"""

    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    OLLAMA_API = os.getenv(
        "OLLAMA_API", "default_api_url"
    )  # Set a default if not provided
    MODEL_NAME = os.getenv("MODEL_NAME", "llama3.1:8b")
    DATA_DIR = BASE_DIR / "data"

    @classmethod
    def validate(cls):
        """Ensure that required settings are available."""
        sage_logger.info("Validating Configuration...")
        try:
            if cls.OLLAMA_API is None:
                raise sage_logger("OLLAMA_API is not set in environment variables")

            if cls.DATA_DIR is None:
                raise sage_logger("Foldername is not set in environment variables")

        except App_ai_Exception as e:
            sage_logger.error(f"Configuration Validation Error: {str(e)}")
            raise

    @classmethod
    def display(cls):
        """Display configuration for debugging purposes."""
        # Define ANSI color codes
        BLUE = "\033[94m"  # Blue for labels
        YELLOW = "\033[93m"  # Yellow for variable values
        RESET = "\033[0m"  # Reset color to default
        sage_logger.info("Configuration Details:")
        sage_logger.info(f"{YELLOW}Base Directory:{RESET} {BLUE}{cls.BASE_DIR}{RESET}")
        sage_logger.info(f"{YELLOW}Ollama API:{RESET} {BLUE}{cls.OLLAMA_API}{RESET}")
        sage_logger.info(f"{YELLOW}Model Name:{RESET} {BLUE}{cls.MODEL_NAME}{RESET}")
        sage_logger.info(f"{YELLOW}Data Directory:{RESET} {BLUE}{cls.DATA_DIR}{RESET}")


if __name__ == "__main__":
    # Config.validate()
    # Config.display()
    pass
