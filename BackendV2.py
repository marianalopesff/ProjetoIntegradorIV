from flask import Flask, request, render_template
from analise import analisar_texto

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        texto = request.form["texto"]
        resultado = analisar_texto(texto)
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)