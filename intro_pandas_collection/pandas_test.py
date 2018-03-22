import pandas as pd
#import numpy as np
#%matplotlib inline

# Read data from data/coffees.csv
data = pd.read_csv("C:\\Users\\ccbre\\Documents\\Data Science Projects\\coffees.csv")

# .head()
head = data.head()

#.loc or .iloc
a = data.loc[2]

# [] indexing on a series
b = data.coffees[:5]

# data set length
#print(len(data))

# .describe
c = data.describe()

# .isnull() and boolean indexing with []
d = data[data.coffees.isnull()]

#print variable
print(d)
