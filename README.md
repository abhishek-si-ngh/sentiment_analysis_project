# 💬 Sentiment Analysis App with Logistic Regression

This project is a web-based Sentiment Analyzer trained on IMDb, Amazon, and Twitter datasets. It uses TF-IDF vectorization and Logistic Regression to classify reviews as positive or negative.

## 📌 Features
- Preprocessing with NLTK stopwords
- Combined dataset from IMDb, Amazon, Twitter
- TF-IDF + Logistic Regression Model
- Flask-based responsive UI (Bootstrap)
- Git LFS used for model tracking
- Hosted on Render

## 🚀 Getting Started

### Requirements
- Python 3.10+
- `requirements.txt` packages

### Run Locally
```bash
git clone https://github.com/abhishek-si-ngh/sentiment_analysis_project.git
cd sentiment_analysis_project
pip install -r requirements.txt
cd app
python app.py
```

### 📂 Folder Structure
```
sentiment_analysis_project/
├── app/
│   ├── static/
│   ├── templates/
│   └── app.py
├── model/
├── notebook/
├── requirements.txt
├── Procfile
├── README.md
```

## 🌐 Live Demo
Deployed on Render: [https://sentiment-analyzer-ptk6.onrender.com]

## 📖 Related Tutorial
👉 [Code2Tutorial Guide for Sentiment Analysis](https://code2tutorial.com/tutorial/99c68415-6aef-4f82-80a4-13634ff22169/index.md)
