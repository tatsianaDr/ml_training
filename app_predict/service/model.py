import pickle


class Model:

    def __init__(self, name):
        self.parameters = dict({"name": name})

    def predict(self, review: str):
        raise NotImplementedError()

    def load_model(self, model_path: str):
        raise NotImplementedError()
