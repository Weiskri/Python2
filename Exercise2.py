import pandas as pd
import numpy as np

# Load CSV Data into a Python Sequence Type (List)
print('************************')
df_breweries = pd.read_csv('data/breweries.csv', index_col='brewery_id')
df_beer = pd.read_csv('data/beers.csv', index_col='beer_id')


# Length
stf = len(df_beer)
qtf = len(df_breweries)
print('Beers:', stf)
print('Breweries:', qtf)

# Clean-up Missing Data
df_beer = df_beer.fillna(0)
df_breweries = df_breweries.fillna(0)

# Merge the dataframes
df = df_beer.join(df_breweries, 'brewery_id', lsuffix='_beer', rsuffix='_brewery')

# Display basic data Metrics
print('Record Count: {}' .format(df.shape[0]))
print('Dataset Shape: {}' .format(df.shape))
print(df.head[5])

# Find the Top 10 Beer Styles
df_grouped = df.groupby('style').count()['id'].sort_values(ascending=False)
print(df_grouped.)


