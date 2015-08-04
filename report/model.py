__author__ = 'rain'

import pandas as pd


class Model:
    def __init__(self):
        self.predictor = None
        pass

    def train(self, x_train, y_train):
        """
        :type x_train: pandas.DataFrame
        :type y_train: pandas.DataFrame
        """
        print "Training..."
        raise NotImplementedError()

    def predict(self, test):
        """
        :type test: pandas.DataFrame
        :rtype : pandas.DataFrame
        """
        raise NotImplementedError()


class SimpleModel(Model):

    def train(self, x_train, y_train):
        pass

    def predict(self, test):
        predict_data = pd.DataFrame({'device_id': test['device_id'], 'cookie_id': 'id_3908095'})
        return predict_data
