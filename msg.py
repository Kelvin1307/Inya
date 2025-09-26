from flask import Blueprint, request, jsonify

msg_bp = Blueprint("msg_bp", __name__)

@msg_bp.route("/send-sms", methods=["POST"])
def send_sms():
    data = request.get_json()
    phone = data.get("to")
    text = data.get("body")

    if not phone or not text:
        return jsonify({"error": "Provide 'to' and 'body' in JSON body"}), 400

    # Mock SMS response (replace with real SMS API if needed)
    response = {
        "status": "sent (mock)",
        "to": phone,
        "message": text
    }
    return jsonify(response)
