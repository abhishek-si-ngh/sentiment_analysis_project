from flask import Flask, render_template, request
import joblib
import os

# Load model and TF-IDF vectorizer
model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'model.pkl')
tfidf_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'tfidf.pkl')

model = joblib.load(model_path)
tfidf = joblib.load(tfidf_path)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        review = request.form['review']
        review_vec = tfidf.transform([review])
        result = model.predict(review_vec)[0]
        prediction = "Positive 😊" if result == 1 else "Negative 😞"
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
