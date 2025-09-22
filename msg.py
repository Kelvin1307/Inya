from flask import Blueprint, request, jsonify
from twilio.rest import Client
import os

msg_bp = Blueprint("msg_bp", __name__)

# Load credentials from environment variables
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def log_sms_event(action, detail):
    masked = mask_pii(str(detail))
    print(f"{action}: {masked}")
    
@msg_bp.route("/send-sms", methods=["POST"])
def send_sms():
    try:
        data = request.get_json()
        phone = data.get("to")
        text = data.get("body")

        if not phone or not text:
            return jsonify({"error": "Missing 'to' or 'body'"}), 400

        # Send SMS
        message = client.messages.create(
            body=text,
            from_=TWILIO_PHONE_NUMBER,
            to=phone
        )

        # Respond with message SID
        return jsonify({
            "status": "sent",
            "sid": message.sid,
            "to": phone,
            "message": text
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

