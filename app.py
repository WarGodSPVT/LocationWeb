from flask import Flask, request, jsonify, send_from_directory
from datetime import datetime

app = Flask(__name__)

visitors = []


@app.route("/")
def home():
    return send_from_directory(".", "index.html")


@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json(silent=True) or {}

    # IP seen by the server
    ip = request.remote_addr

    visitor = {
        "name": data.get("name"),
        "ip": ip,
        "time": datetime.now().isoformat()
    }

    visitors.append(visitor)

    print("\n===== VISITOR =====")
    print("Name:", visitor["name"])
    print("IP:", visitor["ip"])
    print("Time:", visitor["time"])

    return jsonify({"status": "received"})


@app.route("/visitors")
def visitors_history():
    print("\n===== VISITOR HISTORY =====")

    for i, visitor in enumerate(visitors, 1):
        print(f"\n{i}.")
        print("Name:", visitor["name"])
        print("IP:", visitor["ip"])
        print("Time:", visitor["time"])

    return jsonify(visitors)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
