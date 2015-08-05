__author__ = 'rain'


class Model:
    def __init__(self):
        self.predictor = None
        self.score = 0

    def predict(self, test):
        """
        :type test: pandas.DataFrame
        :rtype : pandas.DataFrame
        """
        raise NotImplementedError()

    def fit(self):
        raise NotImplementedError()

    def evaluate(self):
        """
        :rtype : float
        """
        raise NotImplementedError()

