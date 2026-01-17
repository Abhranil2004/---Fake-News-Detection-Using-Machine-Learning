# 📰 Fake News Detector for Students  
### AI-Powered News Credibility Checker

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![React](https://img.shields.io/badge/React-JS-61dafb)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Backend-Online-success)
![License](https://img.shields.io/badge/License-Academic-lightgrey)

---

## 🚀 Overview

**Fake News Detector for Students** is a full-stack AI web application that helps students identify whether a news article is **Real** or **Fake** using **Machine Learning and NLP**.

With the rapid spread of misinformation on social media and online platforms, this tool encourages responsible information sharing by providing quick and reliable credibility analysis.

---

## 🎯 Key Features

- ✅ AI-based Fake vs Real news classification  
- 🧠 Machine Learning with NLP (TF-IDF + Classifier)  
- ⚡ Fast and responsive React frontend  
- 🌐 Flask backend with REST API  
- 🟢 Live backend status indicator (health check)  
- 🎨 Modern, futuristic, student-friendly UI  

---

## 🧠 How the System Works

1. User pastes a news article into the web interface  
2. Text is sent to the Flask backend via API  
3. ML model processes the text using TF-IDF  
4. Classifier predicts **Real** or **Fake**  
5. Result and confidence score are shown instantly  

---

## 🛠️ Tech Stack

### Frontend
- React JS  
- HTML5, CSS3  
- JavaScript (ES6+)  

### Backend
- Python  
- Flask  
- Flask-CORS  

### Machine Learning
- Scikit-learn  
- TF-IDF Vectorizer  
- Passive Aggressive Classifier  

### Tools & Platforms
- Kaggle (Dataset & Model Training)  
- GitHub (Version Control & Hosting)  

---

## 📂 Project Structure

```

fake-news-detector/
│
├── backend/
│   ├── app.py
│   ├── fake_news_model.pkl
│   ├── vectorizer.pkl
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
└── README.md

````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/abhranilduttaabhi/fake-news-detector.git
cd fake-news-detector
````

---

### 2️⃣ Backend Setup

```bash
cd backend
pip install -r requirements.txt
python app.py
```

Backend runs at:

```
http://127.0.0.1:5000
```

Health check:

```
http://127.0.0.1:5000/health
```

---

### 3️⃣ Frontend Setup

```bash
cd frontend
npm install
npm start
```

Frontend runs at:

```
http://localhost:3000
```

---

## 🟢 Backend Status Indicator

The UI includes a **live backend health indicator**:

* 🟢 Green light → Backend running
* 🔴 Red light → Backend offline

This improves reliability and user awareness.

---

## 📸 Screenshots
![Home UI](https://github.com/Abhranil2004/---Fake-News-Detection-Using-Machine-Learning/blob/general/Screenshorts/home.png)
![Fake Result](https://github.com/Abhranil2004/---Fake-News-Detection-Using-Machine-Learning/blob/general/Screenshorts/fake.png)
![Real Result](https://github.com/Abhranil2004/---Fake-News-Detection-Using-Machine-Learning/blob/general/Screenshorts/correct.png)

---

## 📊 Results

* Accurate classification of news articles
* Low response time
* Clean and intuitive interface
* Suitable for academic submission, demos, and portfolios

---

## 🔮 Future Enhancements

* 🌍 Multi-language fake news detection
* 📰 News source credibility scoring
* 🤖 AI-generated news summaries
* 📱 Mobile application
* 🔗 Social media integration

---

## 👨‍💻 Developer

**Abhranil Dutta**

* GitHub: [https://github.com/Abhranil2004](https://github.com/Abhranil2004)

---

## 📜 License

This project is developed for **academic and educational purposes**.

---

## 🙏 Acknowledgements

* Kaggle Datasets
* Scikit-learn Documentation
* Python Community
* Open-source contributors

---

⭐ If you like this project, consider starring the repository!
