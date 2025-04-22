from requests.auth import HTTPBasicAuth
from llama_index.llms.ollama import Ollama

from .logger.logger import ai_agent_logger as sage_logger
from .exceptions.exceptions import App_ai_Exception


def ollama_llm_api(model_name: str = None, base_url: str = None):
    try:
        sage_logger.info("Initializing Ollama LLM...")
        sage_logger.debug(f"Model name: {model_name}, Base URL: {base_url}")

        llm = Ollama(model=model_name, base_url=base_url)

        sage_logger.info("Ollama LLM initialized successfully.")
        return llm

    except Exception as e:
        sage_logger.error(f"Failed to initialize Ollama LLM: {e}")
        raise App_ai_Exception(f"OllamaLLM initialization failed: {e}")


if __name__ == "__main__":
    pass
