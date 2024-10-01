from flask import Flask

app = Flask(__name__)

@app.route("/")
def holaMundo():
    return "¡Hola, Mundo!\n"

if __name__ == '__main__':
    app.run(port=8080)