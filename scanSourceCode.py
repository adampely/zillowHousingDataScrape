import re
import numpy
from zillowAPI1 import zillowAPI

streetAddressContainer = '<span itemprop="streetAddress">'
endStreetAddressContainer = '</span><span itemprop="addressLocality">'
zipCodeContainer = '<span itemprop="postalCode" class="hide">'
endZipCodeContainer = '</span></span><span itemprop="geo" itemscope="" itemtype="http://schema.org/GeoCoordinates">'

sourceCode = open('sampleText2.txt').read()
h = sourceCode.find(streetAddressContainer)
streetAddresses=[]
zipCodes=[]
addressStartIndex = [m.start() for m in re.finditer(streetAddressContainer, sourceCode)]
addressEndIndex = [m.start() for m in re.finditer(endStreetAddressContainer, sourceCode)]
addressStartIndex = numpy.array(addressStartIndex) + len(streetAddressContainer)
print(addressStartIndex)
for i in range(len(addressStartIndex)):
    addressString=sourceCode[addressStartIndex[i]:addressEndIndex[i]]
    streetAddresses.append(addressString)

print(streetAddresses)    
zipCodeStartIndex = [m.start() for m in re.finditer(zipCodeContainer, sourceCode)]
zipCodeEndIndex = [m.start() for m in re.finditer(endZipCodeContainer, sourceCode)]

zipCodeStartIndex = numpy.array(zipCodeStartIndex) + len(zipCodeContainer)
for i in range(len(zipCodeStartIndex)):
    zipCodeString=sourceCode[zipCodeStartIndex[i]:zipCodeEndIndex[i]]
    zipCodes.append(zipCodeString)
    
print(zipCodes)

houseList=[]
for i in range(len(streetAddresses)):
    houseList.append(zillowAPI(streetAddresses[i], zipCodes[i]))

address=[]
zipcodes=[]
bathrooms=[]
bedrooms=[]
rent=[]
price=[]
for house in houseList:
    for feature in house:
        #print(feature.nodeName)
        if feature.nodeName == 'street':
            address.append(feature.firstChild.nodeValue)
            print(feature.firstChild.nodeValue)
        if feature.nodeName == 'zipcode':
            zipcodes.append(feature.firstChild.nodeValue)
            print(feature.firstChild.nodeValue)
        if feature.nodeName == 'bathrooms':
            bathrooms.append(feature.firstChild.nodeValue)
            print(feature.firstChild.nodeValue)
        if feature.nodeName == 'bedrooms':
            bedrooms.append(feature.firstChild.nodeValue)
            print(feature.firstChild.nodeValue)
        if feature.nodeName == 'rentzestimate':
            rent.append(feature.childNodes.__getitem__(0).childNodes[0].nodeValue)
            print(feature.nodeName, feature.childNodes.__getitem__(0).childNodes[0].nodeValue)
        if feature.nodeName == 'amount':
            try:
                if float(feature.firstChild.nodeValue)>10000:
                    price.append(feature.firstChild.nodeValue)
                    print(feature.nodeName, feature.firstChild.nodeValue)
            except:
                price.append('na')
            


    