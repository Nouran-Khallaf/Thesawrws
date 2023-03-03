from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    from .words import words
    app.register_blueprint(words, url_prefix = '/')
    return app


