from urllib.request import Request, urlopen
import json

# Let's construct a request with headers
req = Request('https://devnetapi.cisco.com/sandbox/mse/api/config/v1/maps/info/DevNetCampus/DevNetBuilding/DevNetZone')
req.add_header('Authorization', 'Basic bGVhcm5pbmc6bGVhcm5pbmc=')
req.add_header('Accept', 'application/json')

# Actually open the request
response = urlopen(req)

# Read the response into a JSON String
responseString = response.read().decode("utf-8")

#res = json.dump(obj, out, sort_keys=True, indent=4, separators=(',', ': '))
# Print out the response string
#print(responseString)

# Load the JSON string into a JSON object
json_object = json.loads(response_string)
#print(json_object)
print(json.dumps(json_object, sort_keys=True, indent=4))

# Only output what we are interested in - the AP name and IP address
#access_points = json_object['accessPoints']
#for ap in access_points:
#    print('Access Point: ' + ap['name'] + '\t mac: ' + ap['radioMacAddress'])

# Let's close the response we opened
response.close()
