from __future__ import annotations

from flask import Flask, jsonify, render_template, request

from chatbot.logging_utils import log_interaction
from chatbot.model import ChatbotModel


app = Flask(__name__)
chatbot = ChatbotModel(confidence_threshold=0.45)


@app.route("/")
def index() -> str:
    return render_template("index.html")


@app.route("/get_response", methods=["POST"])
def get_bot_response():
    user_message = request.form.get("user_message", "").strip()
    if not user_message:
        return jsonify({"response": "Please enter a message.", "confidence": 0.0})

    result = chatbot.predict(user_message)
    log_interaction(user_message, result)
    return jsonify(
        {
            "response": result.response,
            "intent": result.intent,
            "confidence": round(result.confidence, 3),
            "fallback": result.fallback,
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
