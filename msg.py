from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/send-sms', methods=['POST'])
def send_sms():
    data = request.json
    phone = data.get("to")
    text = data.get("body")

    # Instead of real SMS, just return mock response
    response = {
        "status": "sent (mock)",
        "to": phone,
        "message": text
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
