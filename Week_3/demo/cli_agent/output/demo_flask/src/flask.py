import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    """Root endpoint that returns a welcome message."""
    return "Welcome to the minimal Flask project!"

@app.route('/echo', methods=['POST'])
def echo():
    """Endpoint that echoes back the JSON payload sent in the request."""
    data = request.get_json()
    return jsonify(data)

@app.route('/health')
def health():
    """Health check endpoint that returns the application status."""
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
