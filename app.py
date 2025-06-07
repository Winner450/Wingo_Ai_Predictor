from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return "WinGo AI Predictor is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        numbers = data.get('numbers', [])
        
        # AI-style random logic (can be replaced by ML model)
        prediction = {
            "Size": random.choice(["Big", "Small"]),
            "Colour": random.choice(["Red", "Green", "Violet"]),
            "Number": random.randint(0, 9),
            "Confidence": f"{random.randint(80, 99)}%"
        }
        return jsonify(prediction)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
