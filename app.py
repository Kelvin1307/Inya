from flask import Flask
from sentiment import sentiment_bp
from policy_parser import policy_bp
import os

app = Flask(__name__)
app.register_blueprint(sentiment_bp, url_prefix='/v1/nlp')
app.register_blueprint(policy_bp, url_prefix='/v1/policy')

if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
