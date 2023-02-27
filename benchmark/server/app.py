"""
modules that contains the server logic
"""
import logging
import sys

from flask import Flask, request

from benchmark.services.queue import QueueService
from benchmark.shared.dogefuzz.api import TaskReport

cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None

app: Flask = Flask(__name__)
app.logger.disabled = True
log = logging.getLogger('werkzeug')
log.disabled = True

_queue_service = QueueService()


@app.route('/dogefuzz/webhook', methods=['POST'])
def webhook():
    """
    store webhook info
    """
    body = request.get_json()
    report = TaskReport.from_json(body)
    _queue_service.put(report)
    return '', 200
