
from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    message = data.get("Body", "")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
    )
    reply = response["choices"][0]["message"]["content"]
    return jsonify({"reply": reply})

@app.route("/", methods=["GET"])
def home():
    return "Villa's Bot is running!"
