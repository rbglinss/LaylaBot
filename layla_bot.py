from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Configura chave da OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return "LaylaBot está pronto para responder!"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")

        # Chamada ao OpenAI usando API antiga (0.28)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente amigável chamado LaylaBot."},
                {"role": "user", "content": user_message}
            ]
        )

        return jsonify({"response": response.choices[0].message["content"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
