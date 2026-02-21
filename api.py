from flask import Flask, request, jsonify
import joblib # استفاده از joblib به جای pickle
import traceback
from utils import extract_features

app = Flask(__name__)

# بارگذاری مدل با joblib
try:
    model = joblib.load("model.pkl")
    print("✅ Model loaded successfully using Joblib.")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    traceback.print_exc()

@app.route('/predict', methods=['GET'])
def predict():
    url = request.args.get('url')
    
    if not url:
        return jsonify({'error': 'No URL provided'}), 400

    try:
        features = [extract_features(url)]
        prediction = model.predict(features)[0]
        result_text = "Phishing" if prediction == 1 else "Safe"
        return jsonify({'url': url, 'prediction': result_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("🚀 Server running on http://127.0.0.1:5000")
    app.run(port=5000)