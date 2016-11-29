import sys
sys.path.append('../')

import os
import random
import pickle
from calculateDistance import calcDist, standardize
from tsbtreedb import *

# if folder not exists, create one
# else clear folder
if not os.path.exists('ts_db_index/'):
	os.makedirs('ts_db_index/')
else:
	files = os.listdir('ts_db_index/')
	for f in files:
		os.remove(os.path.join('ts_db_index/', f))

# random sample 20 vantage points and store the id
rand_vantage = random.sample(range(1000), 20)
pickle.dump(rand_vantage, open('vantage_pts.dat', 'wb+'))

for i in rand_vantage:
	ts = pickle.load(open('ts_data/ts_' + str(i) + '.dat', 'rb'))
	db = connect('ts_db_index/ts_' + str(i) + '.db')
	for j in range(1000):
			other_ts = pickle.load(open('ts_data/ts_' + str(j) + '.dat', 'rb'))
			dist = calcDist(ts, other_ts)
			# if j < 100:
			# 	print(dist)
			db.set(dist, str(j))
	db.commit()
	db.close()

