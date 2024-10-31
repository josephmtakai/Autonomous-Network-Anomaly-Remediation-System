from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Mock function to get current anomalies
def get_current_anomalies():
    # This could be from a real-time database or an API
    return [
        {"src_ip": "192.168.1.10", "severity": "high", "action_taken": "blocked"},
        {"src_ip": "192.168.1.15", "severity": "medium", "action_taken": "rerouted"}
    ]

@app.route("/")
def dashboard():
    anomalies = get_current_anomalies()
    return render_template("dashboard.html", anomalies=anomalies)

if __name__ == "__main__":
    app.run(debug=True)
