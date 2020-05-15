import pickle

from service.model import Model


class SVMModel(Model):

    def __init__(self, name):
        super().__init__("SVM")

    def load_model(self, model_path: str):
        with open(model_path, 'rb') as file:
            return pickle.load(file)





