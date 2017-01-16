import pandas as pd
import sqlite3
import os

#csvNamesList = ['houses1.csv', 'houses2.csv', 'houses3.csv']
def csvToSql(databaseName = 'housingData.sqlite', csvNamesList = ['allDurhamData.csv']):
    if not os.path.isfile(databaseName):
        conn = sqlite3.connect('housingData.sqlite')
        for csvName in csvNamesList:
            house_data = pd.read_csv(csvName, index_col=0, thousands=',')
            house_data.to_sql('houses', conn, if_exists='append', index=False)

def main():
    csvToSql()

if __name__ == "__main__": main()