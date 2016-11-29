"""Commandline tool for finding the closest timeseries points to a given timeseries
"""
import sys
sys.path.append('../')

from tsbtreedb import *
from calculateDistance import calcDist, standardize
import pickle
import heapq

if __name__ == '__main__':
	input_file = sys.argv[1]
	num_to_find = int(sys.argv[2])
	input_ts = pickle.load(open(input_file, 'rb'))
	
	# load vantage points
	vantage_pts = []
	vantage_ids = pickle.load(open('vantage_pts.dat', 'rb'))
	# calc dist from input_ts to vantage points
	dist = []
	for i in vantage_ids:
		vt = pickle.load(open('ts_data/ts_' + str(i) + '.dat', 'rb'))
		dist.append((calcDist(vt, input_ts), str(i)))
	# sort vantage points by distance
	dist.sort(key=lambda kv: kv[0])

	# print(dist)
	id_set = set()
	similar_ts_pQ = []
	for i in range(num_to_find):
		cur_dist = dist[i][0]
		cur_vt_id = dist[i][1]
		cur_db = connect('ts_db_index/ts_' + cur_vt_id + '.db')
		# find ts in current circle
		radius = 2 * cur_dist
		dist_ids = cur_db.get_smaller_than(radius)
		cur_db.close()
		# calc distance from input ts to ts in current circle
		for (ds, Id) in dist_ids:
			if Id not in id_set:
				id_set.add(Id)
				cur_ts = pickle.load(open('ts_data/ts_' + Id + '.dat', 'rb'))
				ds_to_input = calcDist(input_ts, cur_ts)
				heapq.heappush(similar_ts_pQ, (-ds_to_input, Id))
				if len(similar_ts_pQ) > num_to_find:
						heapq.heappop(similar_ts_pQ)
	# print(len(similar_ts_pQ))
	print('Closest (up to) ' + str(num_to_find) + ' time series: ', sorted([(-ds, Id) for (ds, Id) in similar_ts_pQ]))

