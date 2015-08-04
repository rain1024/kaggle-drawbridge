__author__ = 'rain'

from model import Model
import pandas as pd
import datetime
from time import *
import numpy


def create_submission(data):
    """
    :type data: pandas.DataFrame
    """
    data.to_csv('../output/submission-{}.csv'.format(strftime("%Y-%m-%d-%H-%M")), header=True, index=False)


def f_05_score(true, predict):
    """
    :rtype : float
    :type predict: list
    :type true: list
    """
    # p = tp / (tp+fp) # precision
    # r = tp / (tp+fn) # recall
    if true == predict:
        p = 1  # precision
        r = 1  # recall
    else:
        p = 0
        r = 0
    b = 0.5
    if b * b * p + r == 0:
        return 0
    else:
        return (1 + b * b) * (p * r) / (b * b * p + r)


def score(true, predict):
    """
    :rtype : float
    :type predict: numpy.ndarray
    :type true: numpy.ndarray
    """
    values = map(f_05_score, true, predict)
    numpy.mean(values)


class Experiment:
    """
    Machine Learning Experiment Interface
    """
    def __init__(self):
        self.model = Model()
        self.description = "awesome-experiment"
        pass

    def set_description(self, description):
        """
        :type description: str
        """
        self.description = description

    def get_data(self):
        print "========================================"
        print "|    Data Gathering & Preparation      |"
        print "========================================"
        raise NotImplementedError()

    def set_model(self, model):
        """
        :type model: Model
        """
        self.model = model

    def run(self):
        self.get_data()
        self.model.fit()
        self.model.evaluate()

    def predict(self):
        test = pd.read_csv('../input/dev_test_basic.csv')
        predict_data = self.model.predict(test)
        time_stamp = datetime.datetime.now().strftime("%Y_%M_%d_%H_%m")
        predict_data.to_csv('../output/submission-{}-{}.csv'.format(time_stamp, self.description),
                            header=True, index=False)

