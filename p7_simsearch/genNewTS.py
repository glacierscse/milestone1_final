import sys
sys.path.append('../')

from calculateDistance import random_ts
import pickle

"""generate a new random time series and store it.
"""

pickle.dump(random_ts(1), open('input_ts.dat', 'wb+'))