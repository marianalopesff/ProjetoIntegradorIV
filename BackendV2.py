from flask import Flask, request, jsonify
from backend.analise import analisar_texto
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite acessos de fora (frontend)

@app.route("/api/analisar", methods=["POST"])
def api_analisar():
    data = request.get_json()
    texto = data.get("texto", "")
    resultado = analisar_texto(texto)
    return jsonify({"resultado": resultado})

if __name__ == "__main__":
    app.run(debug=True)
