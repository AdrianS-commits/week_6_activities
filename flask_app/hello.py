# from flask import current_app as app
from flask import render_template, Blueprint

# Remove this and the subsequent line, left in to show what was here before the Factory Application pattern was applied
# app = Flask(__name__)

# Now creating a blueprint
main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def index():
    return render_template("index.html")




# You need to enter the following in a terminal window for it to work:
# flask --app 'flask_app:create_app()' --debug run