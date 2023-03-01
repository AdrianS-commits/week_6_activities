from flask import current_app as app
from flask import render_template

# Remove this and the subsequent line, left in to show what was here before the Factory Application pattern was applied
# app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
