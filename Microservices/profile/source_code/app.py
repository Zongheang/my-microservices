import platform
import socket
import time
from datetime import datetime, timezone

from flask import Flask, jsonify

app = Flask(__name__)
START_TIME = time.time()


@app.route('/')
def home():
    return app.send_static_file('index.html')


@app.route('/health')
def health():
    return jsonify(
        service='profile',
        status='UP',
        runtime=f'Python {platform.python_version()}',
        hostname=socket.gethostname(),
        uptimeSeconds=int(time.time() - START_TIME),
        timestamp=datetime.now(timezone.utc).isoformat(),
    )


@app.route('/api/hello')
def hello():
    return "Hello from Python Flask Profile Service"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)
