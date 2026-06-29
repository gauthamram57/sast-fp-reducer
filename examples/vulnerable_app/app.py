from flask import Flask, request
import subprocess

app = Flask(__name__)


@app.route("/")
def home():
    return {
        "application": "SAST FP Reducer Demo",
        "status": "running"
    }


@app.route("/health")
def health():
    return {
        "status": "healthy"
    }


@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")

    result = subprocess.check_output(
        f"ping -c 1 {host}",
        shell=True,
        text=True,
    )

    return {
        "output": result
    }


if __name__ == "__main__":
    app.run(debug=True)
