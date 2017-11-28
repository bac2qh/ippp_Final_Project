#!/usr/bin/env python

import pandas as pd
from sodapy import Socrata


client = Socrata("data.cityofchicago.org", None)

'''
results = client.get("6zsd-86xi", limit=2000)
results_df = pd.DataFrame.from_records(results)
results_df
'''

# where = ... select the data you need
# for your reference
# https://pypi.python.org/pypi/sodapy
# http://pythonhosted.org/sodapy/
# check out get function
# here's my updated version and that should return data
# from 08 to 12

results = client.get("6zsd-86xi", where = "year > 2007 and year <2013")
results_df = pd.DataFrame.from_records(results)
results_df
