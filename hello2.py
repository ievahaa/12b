from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

# print(__name__)


if __name__=="__main__":
    app.run()

@app.route("/sveiki")
def saki_sveiki():
    return "sveiki!"