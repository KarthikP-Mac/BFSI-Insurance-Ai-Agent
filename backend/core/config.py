import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Load environment variables from .env file into os.environ for LangChain
load_dotenv()

class Settings(BaseSettings):
    # LLM Settings
    LLM_PROVIDER: str = os.getenv("LLM_PROVIDER", "openai")
    OPENAI_API_KEY: str | None = os.getenv("OPENAI_API_KEY")
    ANTHROPIC_API_KEY: str | None = os.getenv("ANTHROPIC_API_KEY")
    GEMINI_API_KEY: str | None = os.getenv("Gemini_API_KEY")
    GROQ_API_KEY: str | None = os.getenv("GROQ_API_KEY")
    
    # CRAG Settings
    GRADING_THRESHOLD: float = float(os.getenv("GRADING_THRESHOLD", "0.6"))
    
    # API
    PORT: int = int(os.getenv("PORT", "8000"))
    HOST: str = os.getenv("HOST", "0.0.0.0")

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
