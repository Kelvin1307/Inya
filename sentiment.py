from flask import Blueprint, request, jsonify
from textblob import TextBlob

sentiment_bp = Blueprint("sentiment_bp", __name__)

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        sentiment = "positive"
    elif polarity < -0.1:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    return sentiment, round(polarity, 2)

def upsell_hint(text, sentiment):
    keywords = ["upgrade", "additional coverage", "premium", "benefits", "happy", "satisfied"]
    text_lower = text.lower()
    keyword_score = sum(word in text_lower for word in keywords)

    if sentiment == "positive" and keyword_score > 0:
        return "High likelihood of upsell opportunity."
    elif sentiment == "positive":
        return "Upsell possible; highlight additional benefits."
    elif sentiment == "neutral" and keyword_score > 0:
        return "Moderate upsell chance; approach carefully."
    else:
        return "Focus on renewal first; avoid aggressive upsell."

@sentiment_bp.route('/sentiment', methods=['POST'])
def analyze():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "Please provide 'text' in JSON body."}), 400

    text = data['text']
    sentiment, polarity = analyze_sentiment(text)
    suggestion = upsell_hint(text, sentiment)

    return jsonify({
        "sentiment": sentiment,
        "score": polarity,
        "upsell_suggestion": suggestion
    })
