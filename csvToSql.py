import pandas as pd
import sqlite3

conn = sqlite3.connect('housingData.sqlite')
house_data = pd.read_csv('allDurhamData.csv', index_col=0, thousands=',')
house_data.to_sql('housingData.sqlite', conn, if_exists='append', index=False)
'''
colNames = house_data.keys()

conn = sqlite3.connect('housingData.sqlite')
cur = conn.cursor()
# state    city    zipcode    address    zpid    bathrooms    bedrooms    sqft    hometype    zestimate    rentzestimate    real rent

cur.execute('CREATE TABLE IF NOT EXISTS Houses (state TEXT, zipcode INTEGER, )')
'''