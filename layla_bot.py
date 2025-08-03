import os
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Pegando a chave da OpenAI do ambiente
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/')
def home():
    return "LaylaBot with AI is running!"

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get("question", "")

    if not question:
        return jsonify({"error": "Pergunta não enviada"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Pode mudar para gpt-4 se tiver acesso
            messages=[
                {"role": "system", "content": "Você é uma assistente chamada Layla, simpática e clara nas respostas."},
                {"role": "user", "content": question}
            ],
            max_tokens=200
        )

        answer = response['choices'][0]['message']['content'].strip()
        return jsonify({"response": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
