from flask import Blueprint, request, jsonify
import uuid

# Define a blueprint for payments
payments_bp = Blueprint("payments_bp", __name__, url_prefix="/v1/payments")

@payments_bp.route("/initiate", methods=["POST"])
def initiate_payment():
    """
    Mock API for initiating a payment.
    Expects: {
        "policy_number": "AB123456789",
        "amount": 12999,
        "return_url": "https://example/cb"
    }
    Returns: {
        "payment_link": "https://pay.example/xyz",
        "id": "pay_123"
    }
    """
    data = request.get_json()

    # Validate request
    if not data or "policy_number" not in data or "amount" not in data or "return_url" not in data:
        return jsonify({"error": "Invalid request. Required: policy_number, amount, return_url"}), 400

    # Generate mock payment id and link
    payment_id = f"pay_{uuid.uuid4().hex[:8]}"
    payment_link = f"https://pay.example/{payment_id}"

    response = {
        "payment_link": payment_link,
        "id": payment_id
    }

    return jsonify(response), 200
