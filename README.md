# So this is our Final Project's Repository, Enjoy!

# Project Website: https://bac2qh.github.io/ippp_Final_Project/webpage/project_intro.html

### Repo's layout

There are four important folders in this repo. data folder stores
all supporting data; output folder stores all outputs, including maps and plots;
source_code folder is the Jupyter Notebook codes showing both our final results
and the process of our work; finally webpage folder stores our html files.

### Reserch Topic

Our topic is "The relationship between Socioeconomics indicators and Number of
Crimes in Chicago area". The flow of our research can be described as below:

Collecting data => Processing data => plotting data => analyzing data

#### For the collecting data part
we mostly used "Chicago Data Portal". We started off downloading 1.5 GB worth of
data but finally managed to use the portal' API. Saved us tons of time and makes
it easier for others to run our code.

#### Processing data
We used pandas' tools many times throughout the whole project, including
Join and Merge,
Then groupby to aggregate data, and lastly
loc function to mask data or direct apply mask.

#### Plotting data
This was the most intensive part. We have a large volume of data, which
contains 30 types of crimes and 7 types of socioeconomic status.  
We selected 7 major types of crimes and all the socioeconomic status to find their
one to one or one to many relationships.
Functions and loops were used multiple times to accomplish the plotting.

#### Analyzing data
This was the most difficult part. We came in to this project assuming the results
and correlations should be rather obvious and significant, but interestingly,
many of the relationships took some efforts to reveal.
### Please checkout the Jupyter Notebook Finalized versions in source_code for a project walk-through

# More detailed information available via our website
