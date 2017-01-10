import pandas as pd
import numpy as np
import statsmodels.api as sm

#def performLinearRegression(dataCsvFile = 'allDurhamData.csv'):
house_data = pd.read_csv('allDurhamData.csv', index_col=0, thousands=',')
X = house_data[['bedrooms', 'bathrooms', 'sqft']]
house_price = house_data['zestimate']
house_rent = house_data['real rent']
house_price_rent_ratio = house_rent / house_price
print(house_data.head())

#normalize the data
for column_name in X.keys():
    house_data[column_name + '_norm'] = (X[column_name] - np.mean(X[column_name])) / np.std(X[column_name])

#reassign normalized data
Xnorm = house_data[['bedrooms_norm', 'bathrooms_norm', 'sqft_norm']]

est = sm.OLS(house_price, Xnorm).fit()
