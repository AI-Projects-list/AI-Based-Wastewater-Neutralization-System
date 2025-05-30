# 🌊 AI Wastewater Neutralization System

This project monitors and neutralizes dangerous chemicals in small wastewater storage tanks using real-time sensors and an AI-based decision engine. Based on pH, TDS, and ORP readings, the system decides whether to neutralize the water with chemicals, filter it, or take no action.

## 🚀 Features

- 📡 Real-time chemical sensor monitoring (pH, TDS, ORP)
- 🧠 AI decision engine using scikit-learn (RandomForest)
- 💧 Automatic control of chemical injection or filtering
- 🌐 Web dashboard with live sensor data and action logs
- 📦 Modular: ESP32 firmware, Flask backend, React frontend

## 🧱 Project Structure
```plaintext
ai-neutralizer/
├── ai_model/ # AI model training and dataset
│ ├── train_model.py
│ └── sensor_data.csv
│
├── backend/ # Flask API backend
│ ├── app.py
│ └── model.pkl
│
├── frontend/ # React-based dashboard
│ └── src/
│ ├── App.js
│ ├── index.js
│ └── Dashboard.js
│
├── hardware/ # ESP32 firmware
│ └── esp32_neutralizer.ino
│
├── README.md
└── requirements.txt



## ⚙️ Tech Stack

- ESP32, pH/TDS/ORP sensors
- Python, Flask, scikit-learn
- React.js (Vite or Create React App)
- PostgreSQL (or SQLite for local dev)

## 🧪 AI Model Logic

Trained on historical chemical sensor readings labeled with:
- `neutralize`: Inject chemical to restore safe pH
- `filter`: Open valve to filter contaminants
- `safe`: No action

## 🔌 Hardware Flow

```text
[Sensors] → [ESP32] → [Flask API] → [AI Decision] → [Control: Pump/Valve]
                                       ↓
                               [Log to Database]



---

## 🔧 Backend (Flask) Suggestions

**Endpoints**
- `POST /analyze` → takes pH, TDS, ORP → returns `action`
- `GET /log` → returns historical logs in JSON
- `GET /status` → health check

**Features to Add**
- SQLite/PostgreSQL connection instead of CSV
- Basic authentication with API key
- CORS enabled for frontend requests

**requirements.txt**
```txt
Flask
pandas
scikit-learn
joblib
flask-cors
