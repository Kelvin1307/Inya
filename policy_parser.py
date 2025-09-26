from flask import Flask, request, jsonify, Blueprint
from PyPDF2 import PdfReader
import re
import os
import requests
import tempfile

app = Flask(__name__)
policy_bp = Blueprint("policy_bp", __name__)

def extract_policy_data(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"

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

def log_action(action, detail):
    masked = mask_pii(str(detail))
    print(f"{action}: {masked}")

@policy_bp.route('/parse', methods=['POST'])
def parse_policy():
    file_url = request.json.get('file_url')

    # Check if it's a web URL
    if file_url and file_url.startswith(('http://', 'https://')):
        try:
            response = requests.get(file_url)
            response.raise_for_status()
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
                tmp_file.write(response.content)
                tmp_pdf_path = tmp_file.name
            data = extract_policy_data(tmp_pdf_path)
            os.remove(tmp_pdf_path)
        except Exception as e:
            return jsonify({"error": f"Failed to download or parse PDF: {str(e)}"}), 400
    elif file_url and os.path.exists(file_url):
        data = extract_policy_data(file_url)
    else:
        return jsonify({"error": "PDF file not found"}), 400

    log_action("policy_parsed", data)
    return jsonify(data)
def mask_pii(text):
    text = re.sub(r'\b\d{8,}\b', lambda x: '*' * (len(x.group()) - 2) + x.group()[-2:], text)
    text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', '[masked-email]', text)
    text = re.sub(r'[A-Z0-9]{8,}', '[masked-id]', text)
    text = re.sub(r'([A-Z][a-z]+)', '[masked-name]', text)
    return text
# ...existing code...
if __name__ == '__main__':
    app.run(debug=True, port=5000)
