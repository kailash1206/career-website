from logging import debug
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
  return "Hello, Kailash"


if __name__ == "__main__":
  app.run(port=8080, host="0.0.0.0", debug=True)