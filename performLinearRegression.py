import pandas as pd
import numpy
import statsmodels.api as sm
import matplotlib.pyplot as plt


#def performLinearRegression(dataCsvFile = 'allDurhamData.csv'):
house_data = pd.read_csv('allDurhamData.csv', index_col=0, thousands=',')
#house_data_sql = house_data.to_sql('house_data')
X = house_data[['bedrooms', 'bathrooms', 'sqft']]
house_price = house_data['zestimate']
house_rent = house_data['real rent']
house_price_rent_ratio = house_rent / house_price
sortedByBedrooms = [];
numBedrooms = [];
for i in sorted(house_data.bedrooms.unique()):
    numBedrooms.append(i)
    valList = numpy.array(list(house_data.zestimate[list(house_data.bedrooms == i)]))
    valList = valList[~numpy.isnan(valList)]
    sortedByBedrooms.append(valList)

    
plt.subplot(3,1,1)
plt.plot(X['sqft'], house_price, 'ro')
plt.subplot(3,1,2)
plt.boxplot(sortedByBedrooms)
#plt.xticks(numBedrooms)
plt.subplot(3,1,3)
#plt.boxplot(X['bathrooms'], house_price)
plt.show()
print(house_data.head())

#normalize the data
for column_name in X.keys():
    house_data[column_name + '_norm'] = (X[column_name] - np.mean(X[column_name])) / np.std(X[column_name])

#reassign normalized data
Xnorm = house_data[['bedrooms_norm', 'bathrooms_norm', 'sqft_norm']]

est = sm.OLS(house_price, Xnorm).fit()


