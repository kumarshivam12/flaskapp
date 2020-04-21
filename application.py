
from flask import Flask, render_template

application = Flask(__name__)


@application.route("/home")
def root():
    return render_template("index.html")


@application.route("/hello")
def index():
    return "Hello World from Flask Hello Page."

if __name__ == "__main__":
    application.debug=True
    application.run()
