from urllib.request import Request, urlopen
import json

# Let's construct a request with headers
req = Request('https://64.103.26.61/api/contextaware/v1/maps/info/Moscone/MosconeWest/DevNetLive')
req.add_header('Authorization', 'Basic bGVhcm5pbmc6bGVhcm5pbmc==')
req.add_header('Accept', 'application/json')

# Actually open the request
response = urlopen(req)

# Read the response into a JSON String
responseString = response.read().decode("utf-8")

#res = json.dump(obj, out, sort_keys=True, indent=4, separators=(',', ': '))
# Print out the response string
#print(responseString)

# Load the JSON string into a JSON object
jsonObject = json.loads(responseString)
print(json.dumps(jsonObject, sort_keys=True, indent=4))

# Only output what we are interested in - the AP name and IP address
#accessPoints = jsonObject['Floor']['AccessPoint']
#for ap in accessPoints:
    #print('Access Point: ' + ap['name'] + '\t ip: ' + ap['ipAddress'])

# Let's close the response we opened
response.close()
