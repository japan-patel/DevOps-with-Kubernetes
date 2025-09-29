import os
from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    custom_port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=custom_port)