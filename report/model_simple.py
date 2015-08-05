from score import Score

__author__ = 'rain'

from model import Model
import pandas as pd


class ModelSimple(Model):

    def fit(self):
        pass

    def train(self, x_train, y_train):
        pass

    def predict(self, x_test):
        predict_data = pd.DataFrame({'device_id': x_test['device_id'], 'cookie_id': 'id_2404082'})
        return predict_data

    def evaluate(self):
        test_input = pd.read_csv('../input/local_test_input.csv')
        test_output_true = pd.read_csv('../input/local_test_output.csv')
        test_output_predict = self.predict(test_input)
        if test_output_true.shape != test_output_predict.shape:
            raise RuntimeError('Size of predict is not equal size of true')
        merge_output = pd.merge(test_output_true, test_output_predict, on='device_id', suffixes=['_true', '_predict'])
        true = map(lambda x: x.split(' '), merge_output['cookie_id_true'].values)
        predict = map(lambda x: x.split(' '), merge_output['cookie_id_predict'].values)
        score = Score.mean_f_measure(true, predict, 0.5)
        print "Evaluate:", score
