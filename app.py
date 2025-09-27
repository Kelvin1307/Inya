from flask import Flask
from sentiment import sentiment_bp
from msg import msg_bp
from policy_parser import policy_bp
from payments import payments_bp

app = Flask(__name__)

# Register blueprints with prefixes
app.register_blueprint(sentiment_bp, url_prefix="/v1/sentiment")
app.register_blueprint(msg_bp, url_prefix="/v1/msg")
app.register_blueprint(policy_bp, url_prefix="/v1/policy")
app.register_blueprint(payments_bp, url_prefix="/v1/payments")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
