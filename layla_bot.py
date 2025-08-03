import os
from flask import Flask
import openai

app = Flask(__name__)

# Pega a chave da variável de ambiente no Render
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return "LaylaBot está pronto para responder!"

@app.route("/ask/<question>")
def ask(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente amigável chamado LaylaBot."},
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"Ocorreu um erro: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
