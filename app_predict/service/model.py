import pickle


class Model:

    def __init__(self, name):
        self.parameters = dict({"name": name})


    def predict(self, review: str):
        raise NotImplementedError()


    def load_classifier(self, model_path: str):
        raise NotImplementedError()


    def load_preprocessor(self, preprocessing: str):
        raise NotImplementedError()


    def make_prediction(self, model, preprocessing, review: str):
        raise NotImplementedError()
