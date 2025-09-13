from flask import Flask, request, jsonify
from PyPDF2 import PdfReader
import re

app = Flask(__name__)

@app.route('/v1/policy/parse', methods=['POST'])
def parse_policy():
    file_url = request.json.get('file_url')
    
    # For simplicity, mock reading PDF by using a fixed local file
    # (In real solution, download the file from file_url or accept file upload)
    
    sample_data = {
        "policy_number": "AB123456789",
        "policy_type": "Motor Comprehensive",
        "insurer_name": "Sample Insurance Co.",
        "customer_name": "Riya Sharma",
        "customer_contact": "+91-90000-00000",
        "asset_details": {
            "make": "Maruti",
            "model": "Baleno",
            "year": 2021,
            "registration_number": "KA01AB1234"
        },
        "coverage_summary": ["OD", "Third Party", "PA cover"],
        "expiry_date": "2025-10-15",
        "premium_amount": 12999,
        "no_claim_bonus_percent": 25,
        "last_payment_date": "2024-10-10",
        "eligible_upsell": ["Zero Depreciation", "Roadside Assistance", "Return to Invoice"],
        "payment_link": "https://pay.example.com/renew123"
    }
    
    return jsonify(sample_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
