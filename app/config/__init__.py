from os import getenv

class BaseConnfig:
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False


class DevelopmentConfig(BaseConnfig):
    pass

enviroment = {
    'development': DevelopmentConfig
}