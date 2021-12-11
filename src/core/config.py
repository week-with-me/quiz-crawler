from pydantic import BaseSettings


class Settings(BaseSettings):
    URL: str
    LEVEL: str
    API_KEY: str
    API_URL: str
    DRIVER_PATH: str
    LOCAL_DRIVER_PATH: str
    BINARY_DRIVER_PATH: str
    
    class Config:
        env_file = '.env'
        
        
settings = Settings()