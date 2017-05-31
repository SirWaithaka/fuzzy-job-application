"""
Configurations
"""

class Config:
    DEBUG=False

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_ECHO=True

class ProductionConfig(Config):
    SQLALCHEMY_ECHO=False

app_config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
