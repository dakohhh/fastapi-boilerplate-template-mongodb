from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ENVIRONMENT: str

    APP_NAME: str = "BOILERPLATE TEMPLATE API"

    model_config = SettingsConfigDict(env_file=".env")

# Development-specific settings
class DevelopmentSettings(Settings):
    OPTION: str = 'development_value'

# Production-specific settings
class ProductionSettings(Settings):
    OPTION: str = 'production_value'



# Determine environment and choose appropriate settings
import os

if os.getenv("ENVIRONMENT") == "development":
    settings = DevelopmentSettings()
else:
    settings = ProductionSettings()
