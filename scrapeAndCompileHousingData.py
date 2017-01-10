from requestBasedScrape import requestBasedScrape
from zillowAPI3 import retrieveHouseData
import csv



def scrapeAndCompileHousingData(url =  "http://www.zillow.com/homes/for_rent/Durham-NC/house,mobile,townhouse_type/24457_rid/36.127337,-78.64975,35.842308,-79.118729_rect/10_zm/", pages = 8):
    for page in range(pages):
        print('starting page :', page)
        if page == 0:
            originalUrl = url
        url = originalUrl+str(page+1)+'_p/'
        addresses, zipCodes, realRent = requestBasedScrape(url)
        
        houses = []
        
        for n in range(len(addresses)):
            houseData = retrieveHouseData(addresses[n], zipCodes[n])
            houses.append(houseData)
        print('length address=', len(addresses))
        
        success = 0
        iteration=0
        with open('houses' + str(page+1) + '.csv', 'w', newline='') as csvfile:
            housewriter = csv.writer(csvfile, delimiter=',')
            while success == 0:
                try:
                    keys = list(houses[iteration].keys())
                    keys.append('real rent')
                    housewriter.writerow(keys)
                    success = 1
                except:
                    iteration = iteration+1
                    pass
                    
            for n in range(len(houses)):
                try:
                    values = list(houses[n].values())
                    values.append(realRent[n])
                    housewriter.writerow(values)
                except:
                    pass
        
    print('done')

def main():
    scrapeAndCompileHousingData()

if __name__ == "__main__": main()