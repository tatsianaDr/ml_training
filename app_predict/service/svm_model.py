import pickle

from service.model import Model


class SVMModel(Model):

    def __init__(self, name):
        super().__init__("SVM")

    def load_classifier(self, model_path: str):
        with open(model_path, 'rb') as file:
            return pickle.load(file)


    def make_prediction(self, classifier, preprocessing, review: str):
        return classifier.predict(preprocessing.transform([review]))

    def load_preprocessor(self, preprocessing_path: str):
        with open(preprocessing_path, 'rb') as file:
            return pickle.load(file)





