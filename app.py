from flask import Flask, request, jsonify
from PyPDF2 import PdfReader
import re
import os

app = Flask(__name__)

def extract_policy_data(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"

    # Regex patterns for common fields
    patterns = {
        "policy_number": r"(?:Policy\s*Number|Policy\s*No\.?)\s*[:\-]?\s*([A-Z0-9\-]+)",
        "policy_type": r"(?:Policy\s*Type)\s*[:\-]?\s*([A-Za-z ]+)",
        "insurer_name": r"(?:Insurer|Company)\s*[:\-]?\s*([A-Za-z &]+)",
        "customer_name": r"(?:Customer\s*Name|Proposer)\s*[:\-]?\s*([A-Za-z ]+)",
        "customer_contact": r"(?:Mobile|Phone|Contact)\s*[:\-]?\s*(\+?\d{7,15})",
        "registration_number": r"(?:Registration\s*Number|Regn\. No)\s*[:\-]?\s*([A-Z0-9\-]+)",
        "expiry_date": r"(?:Expiry\s*Date|Valid\s*Till)\s*[:\-]?\s*([0-9]{2}[-/][0-9]{2}[-/][0-9]{4})",
        "premium_amount": r"(?:Premium\s*Amount|Total\s*Premium)\s*[:\-₹]?\s*([\d,]+)"
    }

    extracted = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            extracted[key] = match.group(1).strip()

    return extracted


@app.route('/v1/policy/parse', methods=['POST'])
def parse_policy():
    file_url = request.json.get('file_url')

    # Expecting local path for now
    if not file_url or not os.path.exists(file_url):
        return jsonify({"error": "PDF file not found"}), 400

    data = extract_policy_data(file_url)

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

