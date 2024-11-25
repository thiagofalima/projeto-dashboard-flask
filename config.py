import os.path

class Config:

    CSRF_ENABLE = True
    SECRET = "secret"
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    TEMPLATE_FOLDER = os.path.join(ROOT_DIR, "templates")
    APP = None

class DevelopmentConfig(Config):
    DEBUG = True
    IP_HOST = "localhost"
    PORT_HOST = 8000
    URL_MAIN = f"http://{IP_HOST}/{PORT_HOST}"
    SQLALCHEMY_DATABASE_URI = "pass"

class TestingConfig(Config):
    DEBUG = False
    TESTING = True
    IP_HOST = "192.0.0.1"
    PORT_HOST = 8080
    URL_MAIN = f"http://{IP_HOST}/{PORT_HOST}"
    SQLALCHEMY_DATABASE_URI = "pass"

class ProductionCongif(Config):
    DEBUG = False
    TESTING = False
    IP_HOST = "192.0.5.1"
    PORT_HOST = 8080
    URL_MAIN = f"http://{IP_HOST}/{PORT_HOST}"
    SQLALCHEMY_DATABASE_URI = "pass"


app_config = {
    "development": DevelopmentConfig(),
    "testing": TestingConfig(),
    # "production": ProductionConfig(), goes automatically
}

app_active = os.getenv("FLASK_ENV")
if app_active is None:
    app_active = "development"







