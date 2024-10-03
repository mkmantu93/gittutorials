import redis
from flask import Flask

app = Flask(__name__)

# Adjust the connection to use the service name
cache = redis.Redis(host='redis', port=6379, db=0)

@app.route('/')
def hello():
    try:
        count = cache.incr('hits')
        return f'Hello World! This page has been viewed {count} times.'
    except redis.ConnectionError as e:
        return f'Could not connect to Redis: {e}', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
