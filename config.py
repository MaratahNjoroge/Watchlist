import os

class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('0e7deea64a29555c30a3ace4d2393c7b')
    SECRET_KEY = os.environ.get('SECRET_KEY')
class ProdConfig(Config):
    '''
    Production configuration child class
   
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
 'development' : DevConfig,
 'production' : ProdConfig
}