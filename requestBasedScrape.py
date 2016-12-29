import requests
from bs4 import BeautifulSoup

def requestBasedScrape(url = "http://www.zillow.com/homes/for_rent/Durham-NC-27701/house,condo,apartment_duplex,mobile,townhouse_type/69485_rid/36.031124,-78.84244,35.959876,-78.959684_rect/12_zm/"):
    r = requests.get(url)
    #<div class="zsg-photo-card-content zsg-aspect-ratio-content" itemscope="" itemtype="http://schema.org/SingleFamilyResidence"><span class="hide" itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress"><span itemprop="streetAddress">401 Gray Ave</span>
    
    soup = BeautifulSoup(r.content)
    
    soup.find_all("div")
    addresses=[]
    zipCodes=[]
    realRent=[]
    for item in soup.find_all("div"):
        try:
            if item.get("class")[0] == "zsg-photo-card-content":
                print(item)
                itemExample=item
                for spanItem in itemExample.find_all("span"):
                    try:
                        if spanItem.get("itemprop") == "streetAddress":
                            addresses.append(spanItem.text)
                        elif spanItem.get("itemprop") == "postalCode":
                            zipCodes.append(spanItem.text)
                        elif spanItem.get("class")[0] == "zsg-photo-card-price":
                            print('found realRent')
                            realRent.append(spanItem.text.replace('/mo','').replace('$',''))
                    except:
                        pass
        except:
            pass
    
            #print(item.get("class")[0])

    
    return addresses, zipCodes, realRent