
from flask import Flask, request, jsonify
import os
import openai

app = Flask(__name__)

# Configuração da API OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return "LaylaBot está pronto para responder!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message")

    if not message:
        return jsonify({"error": "Mensagem não fornecida"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}]
        )
        answer = response["choices"][0]["message"]["content"]
        return jsonify({"response": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
