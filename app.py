from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'DRM BOT made by Shuaib Siddiqui Working...'


if __name__ == "__main__":
    app.run()
