from app import app
from flask import jsonify
from datetime import datetime

@app.route("/healthcheck")
def healthcheck():
    current_time = datetime.now().isoformat()
    response = {
            'status': 'healthy',
            'timestamp': current_time
    }
    return jsonify(response), 200

