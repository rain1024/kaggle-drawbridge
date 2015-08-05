import datetime
from repository import Repository

__author__ = 'rain'

from experiment import Experiment
import pandas as pd


class KaggleExperiment(Experiment):
    def __init__(self):
        Experiment.__init__(self)
        self.train = None

    def kaggle_predict(self):
        test = pd.read_csv('../input/dev_test_basic.csv')
        Repository.set_data('submission', self.model.predict(test))
        self.create_submission()

    def create_submission(self):
        submission = Repository.get_data('submission')
        time_stamp = datetime.datetime.now().strftime("%Y_%M_%d_%H_%m")
        file_name = '../output/{}-submission-{}.csv'.format(time_stamp, self.description)
        submission.to_csv(file_name, header=True, index=False)
        print "Submission file", file_name, "is created."

    def get_data(self):
        pass
