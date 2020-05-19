from service.model import Model

from tensorflow.keras import models
from pickle import load

import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from src import metrics


class MLPModel(Model):

    def __init__(self, name):
        super().__init__("MLP")


    def load_classifier(self, model_path: str):
        with open(model_path, 'rb') as file:
            return models.load_model(file, custom_objects={"get_f1": metrics.get_f1})


    def load_preprocessor(self, preprocessing_path: str):
        with open(preprocessing_path, 'rb') as file:
            return load(file)


    def make_prediction(self, classifier, preprocessing, review: str):
        return classifier.predict_classes(preprocessing.transform([review]))




