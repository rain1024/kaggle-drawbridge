from repository import Repository
from model_simple import ModelSimple

__author__ = 'rain'


class ModelNaive(ModelSimple):
    def predict(self, x_test):
        desktops = Repository.get_data('desktops')
        mobiles_sample = x_test
        merge_key = 'anonymous_c2'
        mobiles_sample = mobiles_sample[['device_id', merge_key]].set_index(
            [merge_key, 'device_id'])
        desktops_sample = desktops[['cookie_id', merge_key]].set_index([merge_key])
        merge_data = mobiles_sample.join(desktops_sample).reset_index(1)
        print merge_data
        return merge_data
