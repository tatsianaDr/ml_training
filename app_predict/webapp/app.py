import re

from flask import Flask, request, render_template
import sklearn
import pickle


app = Flask(__name__, template_folder='templates')

with open ('webapp/model/model_sentiment_prediction.pkl', 'rb') as file:
    classifier = pickle.load(file)


@app.route('/')
def welcome():
    return render_template('main.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        review = request.json['review']
        return {'Prediction': predict_sentiment(review)}


def predict_sentiment(review):
    try:
        prediction = list(classifier.predict([preprocessing_text(review)]))
        if prediction[0] == 0:
            pred_text = 'Negative'
        else:
            pred_text = 'Positive'
        return pred_text
    except:
        return 'Error'

# function for preprocessing
def clean_html_string(review):
    return re.sub(r'<br.*?>', ' ', review)

def split_digit_letters_string(review):
    review = re.sub(r'(\d+)', r' \1 ', review)
    return re.sub(r'_+', r' ', review)

def preprocessing_text(review):
    return clean_html_string(split_digit_letters_string(review.lower()))


if __name__ == '__main__':
    app.run(host='0.0.0.0')




