import traceback

from flask import Flask, jsonify, request
import pickle
import sklearn
import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from service import model
from service import svm_model


app = Flask(__name__)


@app.before_first_request
def load_model_to_app():
    # Load the model
    app.classifier = load_model(svm_model.SVMModel, 'service/model/model_sentiment_prediction.pkl')


@app.route('/predict', methods=['POST'])
def review_classifier():
    if request.method == 'POST':
        review = request.json['review']
        return predict_sentiment(app.classifier, review)


def load_model(model, model_path):
    # Load the model
    return model.load_model(model, model_path)


def predict_sentiment(model, review):
    # Make the prediction
    try:
        prediction = list(model['model'].predict([review]))
        if prediction[0] == 0:
            pred_text = 'Negative'
        else:
            pred_text = 'Positive'
        return jsonify({'Prediction': pred_text})
    except:
        return traceback.format_exc()

if __name__ == '__main__':
    app.run(host='0.0.0.0')