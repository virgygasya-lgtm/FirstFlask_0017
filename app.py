
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet", methods=["POST"])
def greet():
    name = request.form.get("name")
    if not name:
        name = "Anonim"
    return f"<h2>Halo, {name}! Selamat datang di Flask First App 🚀</h2>"

if __name__ == "__main__":
    app.run(debug=True)