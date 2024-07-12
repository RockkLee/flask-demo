# db url
_USER = "postgres"
_PASSWORD = "1234"
# _IP = "db" # Run the app in docker
_IP = "localhost"  # Run the app locally
DATABASE_URI = 'postgresql://%s:%s@%s:5432/postgres' % (_USER, _PASSWORD, _IP)

# flask-restx(swagger) config
SWAGGER_DOC = "/docs"  # to disable swagger doc, set it to "False"
# flask config
if __name__ == "__app__":
    flask_config = "flask_demo.config.DevConfig"
else:
    flask_config = "flask_demo.config.TestConfig"


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ERROR_404_HELP = False


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    DEBUG = False


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    DEBUG = True


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    DEBUG = True
