from flask import Flask
from sentiment import sentiment_bp
from msg import msg_bp
from policy_parser import policy_bp

app = Flask(__name__)

app.register_blueprint(sentiment_bp)
app.register_blueprint(msg_bp)
app.register_blueprint(policy_bp)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
