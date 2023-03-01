from flask import Flask


def create_app():
    """Create and configure the Flask app"""
    app = Flask(__name__)

    # Registering the blueprint before returning the Flask app object.
    from flask_app.hello import main_bp
    app.register_blueprint(main_bp)

    
#     In order to generate a secret key, enter the following in terminal:
#     python
#       >> import secrets
#       >> secrets.token_urlsafe(16)


    app.config["SECRET_KEY"] = 'Wd-oxH5_zAOO6qveNAQiQg'

    # Include the routes from app.py
    with app.app_context():
        from . import hello

    return app