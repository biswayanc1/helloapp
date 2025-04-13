from flask import Flask
from prometheus_client import generate_latest, Counter

app = Flask(__name__)

@app.route('/')
def home():
    return "Biswayan says hello!"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")