__author__ = 'rain'

mobiles_sample = mobiles_sample.loc[:200]

for i in range(mobiles.shape[0] - 1):
    mobile = mobiles_sample.loc[i]
    print 'Index:', i
    if mobile.anonymous_c1 != '-1':
        print 'Feature:', mobile.anonymous_c1
        print desktops[desktops.anonymous_c1 == mobile.anonymous_c1]

test_size = mobiles_test.shape[0]
import datetime
from time import *
history = []
step = {'start': time(), 'end': 0}
for i in range(test_size - 1):
    mobile = mobiles_test.loc[i]
    if mobile.anonymous_c1 != '-1':
        cookie_id = desktops[desktops.anonymous_c1 == mobile.anonymous_c1].iloc[0]['cookie_id']
        bridges.ix[i]['cookie_id'] = cookie_id
    # update history
    step['end'] = time()
    history.append(step)
    # logging
    print "[{0}] [{1:2.2f}%]: Step {2} in {3} takes {4:.2f} seconds".format(
        strftime("%Y-%m-%d %H:%M:%S"), i * 100.0 / test_size, i, test_size, step['end'] - step['start'])
    # init new step
    step['start'] = time()
