from flask import Flask


def create_app():
    """Create and configure the Flask app"""
    app = Flask(__name__)

    # Include the routes from app.py
    with app.app_context():
        from . import hello

    return app