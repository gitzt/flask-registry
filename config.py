import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    
    @staticmethod
    def init_app(app):
        pass
        
class DevelopmentConfig(Config):
    DEBUG = True
    
class TestingConfig(Config):
    DEBUG = True
    

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    
    'default': DevelopmentConfig
}

