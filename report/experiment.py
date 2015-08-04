__author__ = 'rain'

from model import Model
import pandas as pd
import datetime
from time import *


def create_submission(data):
    data.to_csv('../output/submission-{}.csv'.format(strftime("%Y-%m-%d-%H-%M")), header=True, index=False)


class Experiment:
    def __init__(self):
        self.model = Model()
        self.description = "awesome-experiment"
        pass

    def set_description(self, init_description):
        """
        :type init_description: str
        """
        self.description = init_description

    def set_model(self, init_model):
        """
        :type init_model: Model
        """
        self.model = init_model

    def run(self):
        self.model.train()

    def predict(self):
        test = pd.read_csv('../input/dev_test_basic.csv')
        predict_data = self.model.predict(test)
        time_stamp = datetime.datetime.now().strftime("%Y_%M_%d_%H_%m")
        predict_data.to_csv('../output/submission-{}-{}.csv'.format(time_stamp, self.description),
                            header=True, index=False)
