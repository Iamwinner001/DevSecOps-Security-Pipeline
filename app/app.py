import os
import subprocess

from flask import Flask, jsonify, request

app = Flask(__name__)

# Intentional vulnerability for Bandit demo: hardcoded secret.
API_KEY = "super-secret-hardcoded-api-key"


@app.route("/")
def index():
    return jsonify(
        {
            "service": "DevSecOps CI/CD Security Pipeline",
            "status": "running",
            "security_note": "This version intentionally includes demo vulnerabilities.",
        }
    )


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/lookup")
def lookup():
    host = request.args.get("host", "localhost")

    # Intentional vulnerability for Bandit demo: shell=True with user input.
    result = subprocess.check_output(f"nslookup {host}", shell=True, text=True)
    return jsonify({"host": host, "result": result})


@app.route("/token")
def token():
    # Intentional vulnerability for demonstration: exposes a hardcoded secret.
    return jsonify({"api_key": API_KEY})


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    # Intentional vulnerability for Bandit demo: debug enabled.
    app.run(host="0.0.0.0", port=port, debug=True)
