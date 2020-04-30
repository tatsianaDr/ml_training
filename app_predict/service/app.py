from flask import Flask, request

import pickle
import sklearn

import os, sys, inspect

from waitress import serve

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        review = request.json['review']
        return {'Model' : classifier['metadata'],
                'Prediction': predict_sentiment(review)}


class Model:
    def __init__(self):
        with open('service/model/model_sentiment_prediction.pkl', 'rb') as file:
            self.classifier = pickle.load(file)

my_model = Model()

classifier = my_model.classifier

def predict_sentiment(review):
    try:
        print(review)
        print(classifier['model'])
        prediction = list(classifier['model'].predict([review]))
        if prediction[0] == 0:
            pred_text = 'Negative'
        else:
            pred_text = 'Positive'
        return pred_text
    except:
        return 'Error'


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8000)
    # app.run(host='0.0.0.0')

