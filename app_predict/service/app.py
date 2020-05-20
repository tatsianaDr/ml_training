import logging
import traceback
import json
from logging.handlers import RotatingFileHandler

from flask import Flask, jsonify, request
import pickle
import sklearn
import os, sys, inspect
import tensorflow as tf
from tensorflow.python.keras.backend import set_session


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from service import model
from service import svm_model
from service import mlp_model


app = Flask(__name__)

logger = logging.getLogger('app-logger')
# file_handler = RotatingFileHandler('test.log', maxBytes=10000, backupCount=1)
# logger.addHandler(file_handler)
# logger.setLevel(logging.DEBUG)
file_handler = RotatingFileHandler('test.log', maxBytes=10000, backupCount=1)
handler = logging.StreamHandler()
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
))
handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
))
logger.addHandler(file_handler)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

models_params = {}
models_params['MLP'] = {'class': mlp_model.MLPModel,
                        'model_path': 'service/model/mlp/mlp_final.hdf5',
                        'preprocessor_path': 'service/model/mlp/mlp_preproc.pkl',
                        'info_path': 'service/model/mlp/mlp_model.json'}

models_params['SVM'] = {'class': svm_model.SVMModel,
                        'model_path': 'service/model/svm/svm_final_model.pkl',
                        'preprocessor_path': 'service/model/svm/svm_final_model_preproc.pkl',
                        'info_path': 'service/model/svm/svm_model.json'}

name_model = "MLP"


@app.before_first_request
def load_model_to_app():
    logger.info("Loading the model %s" % (model))
    # Load the model
    try:
        global sess
        global graph
        sess = tf.Session()
        graph = tf.get_default_graph()
        set_session(sess)
        global model_params
        model_params = define_model(name_model)
        print(model_params)
        app.classifier = load_classifier(model_params[0], model_params[1])
        print(app.classifier)
        if model_params[2]:
            app.preprocessor = load_preprocessor(model_params[0], model_params[2])
        else:
            app.preprocessor = None
        logger.info("The model %s loaded." % (model))
    except:
        logger.error("Error %s " % (traceback.format_exc()))


@app.route('/predict', methods=['POST'])
def review_classifier():
    review = request.json['review']
    logger.info("Classifying sentiment review: %s" % (review), )
    if request.method == 'POST':
        return predict_sentiment(model_params[0], app.classifier, app.preprocessor, review)

@app.route('/model', methods=['GET'])
def get_model_info():
    if request.method == 'GET':
        with open(model_params[3], 'rb') as file:
            return json.load(file)


def define_model(name):
    params = models_params[name]
    return params['class'], params['model_path'], params['preprocessor_path'], params['info_path']


def load_classifier(model, model_path):
    # Load the model
    return model.load_classifier(model, model_path)


def load_preprocessor(model, preprocessor_path):
    # Load the model
    return model.load_preprocessor(model, preprocessor_path)


def predict_sentiment(model, classifier, preprocessor, review):
    with graph.as_default():
        set_session(sess)
        # Make the prediction
        try:
            prediction = list(model.make_prediction(model, classifier, preprocessor, review))
            if prediction[0] == 0:
                pred_text = 'Negative'
            else:
                pred_text = 'Positive'
            logger.info("The review has %s sentiment" % (pred_text) )
            return jsonify({'Prediction': pred_text})
        except:
            logger.error("Error %s " % (traceback.format_exc()))
            return traceback.format_exc()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    debug = True

