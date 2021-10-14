from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Teste de Alteração by Pedro Bassetto"

if __name__ == '__main__':
    app.run(debug=True)