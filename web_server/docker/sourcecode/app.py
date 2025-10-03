import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("response.html")

if __name__ == "__main__":
    custom_port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=custom_port)