import ipaddress
import os
import socket

from flask import Flask, jsonify, request

app = Flask(__name__)


def resolve_host(hostname):
    allowed_suffixes = (".example.com", "localhost")
    if hostname != "localhost" and not hostname.endswith(allowed_suffixes):
        raise ValueError("Host is outside the allowed lookup scope.")

    address = socket.gethostbyname(hostname)
    ip = ipaddress.ip_address(address)

    if ip.is_private and hostname != "localhost":
        raise ValueError("Private address lookup is not allowed.")

    return address


@app.route("/")
def index():
    return jsonify(
        {
            "service": "DevSecOps CI/CD Security Pipeline",
            "status": "running",
            "security_note": "Secure version with safer input handling.",
        }
    )


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/lookup")
def lookup():
    host = request.args.get("host", "localhost").strip()
    try:
        address = resolve_host(host)
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400

    return jsonify({"host": host, "address": address})


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    debug = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug)
