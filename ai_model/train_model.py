import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("sensor_data.csv")
X = df[["pH", "TDS", "ORP"]]
y = df["action"]

model = RandomForestClassifier()
model.fit(X, y)
joblib.dump(model, "model.pkl")
