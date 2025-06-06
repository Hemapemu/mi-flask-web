from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>¡Hola desde mi página web con Python y Flask!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
