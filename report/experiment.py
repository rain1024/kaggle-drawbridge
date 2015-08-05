__author__ = 'rain'

from model import Model


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
        raise NotImplementedError()

    def set_model(self, model):
        """
        :type model: Model
        """
        self.model = model

    def run(self):
        print " ====================================== "
        print "|    Data Gathering & Preparation      |"
        print " ====================================== "
        self.get_data()
        print " ====================================== "
        print "|            Model Building            |"
        print " ====================================== "
        self.model.fit()
        print " ====================================== "
        print "|            Model Evaluate            |"
        print " ====================================== "
        self.model.evaluate()
