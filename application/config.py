import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Base configuration"""


class ProductionConfig:
    """Production configuration"""


class DevelopmentConfig:
    """Development configuration"""


class TestingConfig:
    """Testing configuration"""

    TESTING = True
