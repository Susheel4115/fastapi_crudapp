import requests

# using mapquest api for getting the coordinate of perticuller address 

# api Secret Key 
coordinateApiKey = "7G68oEy6Ur4WV86vawBbKbbiOmwGrxh0"

# api end point with query ?location=
coordinateApi = f"http://www.mapquestapi.com/geocoding/v1/address?key={coordinateApiKey}&location="


# it's return the address information along with coordinate of and address 
# It's take 3 parameter and use them as location query for api 

def getCoordinate(addressLine, city, state):
    mainCoordinateApi = f"{coordinateApi}{addressLine},{city},{state}"
    print(mainCoordinateApi)
    r = requests.get(mainCoordinateApi)
    locationData = r.json()["results"][0]["locations"][0]
    return locationData