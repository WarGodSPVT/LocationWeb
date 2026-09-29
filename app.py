from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

visitors = []

@app.route("/")
def home():
    return send_from_directory(".", "index.html")


@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()

    visitor = {
        "name": data.get("name"),
        "latitude": data.get("latitude"),
        "longitude": data.get("longitude"),
        "accuracy": data.get("accuracy"),
        "time": data.get("time")
    }

    visitors.append(visitor)

    print("\n===== NEW VISITOR =====")
    print("Name:", visitor["name"])
    print("Latitude:", visitor["latitude"])
    print("Longitude:", visitor["longitude"])
    print("Accuracy:", visitor["accuracy"], "meters")
    print("Time:", visitor["time"])

    return jsonify({"status": "received"})


@app.route("/visitors")
def get_visitors():
    return jsonify(visitors)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)