"""
modules that contains the server logic
"""
from flask import Flask, request

from benchmark.services.queue import QueueService
from benchmark.shared.dogefuzz.api import TaskReport

app: Flask = Flask(__name__)
_queue_service = QueueService()


@app.route('/dogefuzz/webhook', methods=['POST'])
def webhook():
    """
    store webhook info
    """
    body = request.get_json()
    report = TaskReport.from_json(body)
    _queue_service.put(report)
    return None, 200
