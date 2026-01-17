from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

# Load model and vectorizer
model = pickle.load(open("fake_news_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/")
def home():
    return "Fake News Detector API is running"

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    news_text = data["text"]

    # Transform text
    text_vector = vectorizer.transform([news_text])

    # Prediction
    prediction = model.predict(text_vector)[0]
    confidence = model.decision_function(text_vector)[0]

    result = "Fake News" if prediction == 0 else "Real News"

    return jsonify({
        "prediction": result,
        "confidence": round(abs(float(confidence)), 2)
    })

if __name__ == "__main__":
    app.run(debug=True)
