## Similarity Search
This file provides several functionality, including generate random timeseries data, randomly select vantage timeseries points, calculate distance btw 2 timeseries data, and most importantly find closest timeseries points to a given timeseries input.

### Generate random timeseries data
You can run `genTS.py` to generate randome timeseries data.
```
$ python genTS.py --help

Usage: genTS.py [OPTIONS]

  generate n standardized time series, each stored in a file in ts_data/.

Options:
  -n INTEGER   number of ts to generate, default 1000
  --n INTEGER  number of ts to generate, default 1000
  --help       Show this message and exit.
```
For example, use `python genTS.py --n 500` to generate 500 timeseries data.

The generated data would be stored as `.dat` files in `ts_data\`.

### Generate 
