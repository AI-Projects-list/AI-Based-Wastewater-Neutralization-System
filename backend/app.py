from flask import Flask, request, jsonify
import joblib
import pandas as pd
import datetime

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    X = [[data['ph'], data['tds'], data['orp']]]
    action = model.predict(X)[0]
    log = pd.DataFrame([{
        "timestamp": datetime.datetime.now(),
        "ph": data['ph'],
        "tds": data['tds'],
        "orp": data['orp'],
        "action": action
    }])
    log.to_csv("log.csv", mode='a', header=False, index=False)
    return jsonify({"action": action})
