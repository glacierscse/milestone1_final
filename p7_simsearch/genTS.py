import sys
sys.path.append('../')

from calculateDistance import tsmaker
import pickle
import random

"""This script generate 1000 time series, each stored in a file in ts_data/.
"""

m_a, m_b = 0, 100
s_a, s_b = 0.1, 10
j_a, j_b = 1, 10

m = [random.uniform(m_a, m_b) for i in range(1000)]
s = [random.uniform(s_a, s_b) for i in range(1000)]
j = [random.randint(j_a, j_b) for i in range(1000)]

for i in range(1000):
	with open('ts_data/ts_' + str(i) + '.dat', 'wb+') as f:
		ts = tsmaker(m[i], s[i], j[i])
		pickle.dump(ts, f)

# for i in range(2):
# 	with open('ts_data/ts_' + str(i) + '.dat', 'rb') as f:
# 		ts = pickle.load(f)
# 		print(type(ts))