from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def root():
    return "Hello World from Flask Hello Page"
if __name__ == '__main__':
    app.debug= True
    app.run()