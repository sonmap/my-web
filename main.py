import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>안녕하세요! 첫 페이지입니다.</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
