"""
Configurations
"""

import os

class Config:
    DEBUG=False
    SQLALCHEMY_DATABASE_URI=os.getenv("DATABASE_URL")

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_ECHO=True

class ProductionConfig(Config):
    SQLALCHEMY_ECHO=False

app_config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
