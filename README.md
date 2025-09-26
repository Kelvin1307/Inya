📌 Insurance Renewal & Upsell API

This project provides a set of REST APIs for insurance companies to:

📑 Parse insurance policy PDFs (extract customer + policy details).

💬 Send SMS notifications (via Twilio).

🤖 Perform sentiment analysis on customer responses.

🚀 Features

Policy Parser → Extracts policy number, customer name, expiry date, premium, etc. from PDF files.

Messaging (Twilio) → Sends SMS notifications for renewals/upsells.

Sentiment Analysis → Detects positive/negative/neutral intent from customer replies.

Flask + Gunicorn based microservice, deployable on Render or any cloud provider.

📂 Project Structure
.
├── app.py                # Main Flask entry point
├── sentiment.py          # Sentiment Analysis blueprint
├── msg.py                # SMS Messaging (Twilio) blueprint
├── policy_parser.py      # PDF Policy Parser blueprint
├── requirements.txt      # Python dependencies
├── README.md             # Documentation
⚙️ Installation (Local)

Clone the repo

git clone https://github.com/your-username/insurance-renewal-api.git
cd insurance-renewal-api


Create virtual environment

python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)


Install dependencies

pip install -r requirements.txt


Set environment variables (create .env file or export directly):

export TWILIO_ACCOUNT_SID="your_twilio_sid"
export TWILIO_AUTH_TOKEN="your_twilio_auth_token"
export TWILIO_PHONE_NUMBER="+1234567890"
📡 API Endpoints
1. Policy Parser

POST /v1/policy/parse
Extracts data from PDF insurance policy.

Request:

{
  "file_url": "/path/to/policy.pdf"
}


Response:

{
  "policy_number": "AB123456789",
  "customer_name": "Riya Sharma",
  "expiry_date": "15-Oct-2025",
  "premium_amount": "₹12,999"
}
2. Send SMS

POST /send-sms

Request:

{
  "to": "+919876543210",
  "body": "Your policy expires soon. Renew now!"
}


Response:

{
  "status": "sent",
  "sid": "SMxxxxxxxxxxxx"
}
3. Sentiment Analysis

POST /analyze-sentiment

Request:

{
  "text": "I am happy to renew my policy."
}


Response:

{
  "sentiment": "positive",
  "polarity": 0.85
}
☁️ Deployment on Render

Push code to GitHub.

Create a new Render Web Service → Connect repo.

Set Start Command:

gunicorn app:app --bind 0.0.0.0:$PORT


Add Environment Variables in Render Dashboard:

TWILIO_ACCOUNT_SID

TWILIO_AUTH_TOKEN

TWILIO_PHONE_NUMBER

Deploy 🚀

🛠 Dependencies

Flask

Gunicorn

Twilio

TextBlob (for sentiment)

PyPDF2 (for policy parsing)

Install via:

pip install -r requirements.txt
