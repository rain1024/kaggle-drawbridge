__author__ = 'rain'

import numpy


class Score:
    @staticmethod
    def f_measure(true, predict, b=1.0):
        """
        :type predict: numpy.ndarray
        :type true: numpy.ndarray
        :rtype : float
        """
        # p = tp / (tp+fp) # precision
        # r = tp / (tp+fn) # recall
        if true == predict:
            p = 1  # precision
            r = 1  # recall
        else:
            p = 0
            r = 0
        if b * b * p + r == 0:
            return 0
        else:
            return (1 + b * b) * (p * r) / (b * b * p + r)

    @staticmethod
    def mean_f_measure(true, predict, b=1.0):
        """
        :type true:  numpy.ndarray
        :type predict: numpy.ndarray
        :type b: float
        """
        values = map(lambda x, y: Score.f_measure(x, y, b), true, predict)
        score = numpy.mean(values)
        return score
