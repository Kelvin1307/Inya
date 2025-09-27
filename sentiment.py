# app.py
from flask import Flask, Blueprint, request, jsonify
from textblob import TextBlob

app = Flask(__name__)
sentiment_bp = Blueprint("sentiment_bp", __name__)

from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@sentiment_bp.route("/analyze", methods=["POST"])
def analyze_sentiment(text):
    try:
        # Get JSON input
        data = request.get_json()
        text = data.get("text", "")

        if not text.strip():
            return jsonify({"error": "Text is required"}), 400

        # Sentiment analysis using TextBlob
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity  # -1 (negative) to +1 (positive)

        # Convert polarity to sentiment label
        if polarity > 0:
            sentiment = "positive"
        elif polarity < 0:
            sentiment = "negative"
        else:
            sentiment = "neutral"

        response = {
            "sentiment": sentiment,
            "score": round(polarity, 2)
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
