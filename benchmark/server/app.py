"""
modules that contains the server logic
"""
from flask import Flask, request

from benchmark.services.queue import QueueService

app: Flask = Flask(__name__)
_queue_service = QueueService()


@app.route('/dogefuzz/webhook', methods=['POST'])
def webhook():
    """
    store webhook info
    """
    body = request.get_json()
    _queue_service.put(body)
    return None, 200
