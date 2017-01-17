from urllib.parse import urlencode
from urllib.request import Request
import urllib.request
from bs4 import BeautifulSoup
import collections

def __init__():
    retrieveHouseData()

def retrieveHouseData(streetAddress='401 Gray Ave', zipcode='27701'):
    apiUrl="http://www.zillow.com/webservice/GetDeepSearchResults.htm" 
    apiParam = {'zws-id' : 'X1-ZWz1fdd2duhhjf_6h6e1',
            'address': streetAddress,
            'citystatezip' : zipcode,
            'rentzestimate' : True}
    #Declare and assign value for apiParam variable here
    #Declare and assign value for outputFormat variable forresponse format in querystring
    apiParamsUrl = urlencode(apiParam)
    binary_data = apiParamsUrl.encode('ascii')
    #apiUrl=apiUrl.encode('ascii')
    req=Request(apiUrl, binary_data)
    
    response = urllib.request.urlopen(req)
    #urllib.request.urlopen()
    xml=BeautifulSoup(response.read(),'xml')
    houseData=collections.OrderedDict()
    try:
        houseData['state'] = xml.findAll('state')[0].text
        houseData['city'] = xml.findAll('city')[0].text
        houseData['zipcode'] = xml.findAll('zipcode')[0].text
        houseData['address'] = xml.findAll('street')[0].text
        houseData['latitude'] = xml.findAll('latitude')[0].text
        houseData['longitude'] = xml.findAll('longitude')[0].text
        houseData['zpid'] = xml.findAll('zpid')[0].text
        houseData['bathrooms'] = xml.findAll('bathrooms')[0].text
        houseData['bedrooms'] = xml.findAll('bedrooms')[0].text
        houseData['sqft'] = xml.findAll('finishedSqFt')[0].text
        houseData['homtype'] = xml.findAll('useCode')[0].text
        houseData['taxAssessmentYear'] = xml.findAll('taxAssessmentYear')[0].text
        houseData['taxAssessment'] = xml.findAll('taxAssessment')[0].text
        houseData['zestimate'] = xml.findAll('zestimate')[0].findAll('amount')[0].text
        houseData['rentzestimate'] = xml.findAll('rentzestimate')[0].findAll('amount')[0].text
    except:
        houseData=None
    return houseData
