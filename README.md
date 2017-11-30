# So this is our final project's repo
# ENJOY

The data source we are using are
https://data.cityofchicago.org/view/5cd6-ry5g
for crime data
and
https://data.cityofchicago.org/Health-Human-Services/Census-Data-Selected-socioeconomic-indicators-in-C/kn9c-c2s2
for socioeconomic status
I am working on the api for the crime data.
So plz download the whole 1.5 GB data for now.
We plan to join the two dataset by "community_area number"
and here is a link for community_area code's in Chicago
https://en.wikipedia.org/wiki/Community_areas_in_Chicago

#### Xin 11/26 14:08

So I just found the way to use the Chicago portal's api
Documentation: https://dev.socrata.com/foundry/data.cityofchicago.org/6zsd-86xi
If you scroll all the way down, you will see this code

```
#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.cityofchicago.org", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.cityofchicago.org,
#                  MyAppToken,
#                  userame="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("6zsd-86xi", limit=2000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(result_list)
```
as mentioned in the code above, you can use it without a token,
but for very limited amount of queries.
also, make sure you install sodapy beforehand


#### Xin 11/26 21:55

IUCR codes
https://data.cityofchicago.org/Public-Safety/Chicago-Police-Department-Illinois-Uniform-Crime-R/c7ck-438e

#### Xin 11/27 22:56

I was able to make the api work.
Check out the Final Project.ipynb for details

#### Xin 11/27 22:56

Final_Project_Nov27.ipynb is ready for regression.
(the average level of crime vs the average level of socioeconomic indicators in 2008-2012)

#### Di 11/28 1:08

#### Bin 11/28  10:00

#### Di 11/28 11:46

Created two dataframes: crime_total and crime_type.
crime_total can be used for regression. (NaN not dropped)
crime_type still has a merging problem. (NaN not dropped)

Started a detailed analysis on crime: see Crime_Only_Analysis.

Plan to revise the graph and plot the map for crime, and conduct a similar analysis on socioeconomics data.

#### Xin 11/28 01:31

Dropped NaN (use inplace = True).
merged dataframe for crime_type_reg.
Binbin you should be able to start doing whatever you want at this point.

I will also start looking at geopandas right now.

#### Xin 11/29 22:28

The plotting works are in Crime_Type_plot.ipynb.
Currently working on plotting primary_types in different community_area

#### Xin 11/29 23:10
Got the interactive map for total crime rate.
will be working on primary_types tomorrow.


# Thanks
