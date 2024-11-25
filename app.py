from flask import Flask

# App Factory

def create_app(config):
    # Creating an application
    app = Flask(__name__)

    app.secret_key = config.SECRET
    app.config.from_object(config)
    app.config.from_pyfile("config.py")
    app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI

    # True on Prouction
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    config.APP = app

    # Allowing people to consume my application with APIs

    @app.after_request
    def after_request(response):
        response.headers("Access-Control-Allow-Origin", "*")
        response.headers("Access-Control-Allow-Headers", "Content-Type")


    @app.route('/')
    def index():
        return "oi"

