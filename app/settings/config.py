from pydantic import BaseModel, AnyUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ENVIRONMENT: str

    APP_NAME: str = "BOILERPLATE TEMPLATE API"

    model_config = SettingsConfigDict(env_file=".env")

# Development-specific settings
class DevelopmentSettings(Settings):
    MONGODB_URL: AnyUrl = "mongodb://localhost:27017"
    OPTION: str = 'development_value'

# Production-specific settings
class ProductionSettings(Settings):
    MONGODB_URL: AnyUrl
    OPTION: str = 'production_value'



# Determine environment and choose appropriate settings
import os

if Settings.APP_NAME == "development":
    print("Development settings loaded")
    settings = DevelopmentSettings()
else:
    settings = ProductionSettings()
