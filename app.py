from flask import Flask
from sentiment import sentiment_bp
from policy_parser import policy_bp

app = Flask(__name__)

# Register all Blueprints
app.register_blueprint(sentiment_bp, url_prefix='/v2/senti')
app.register_blueprint(policy_bp, url_prefix='/v1/policy')
app.register_blueprint(msg_bp, url_prefix='/v3/sms')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
