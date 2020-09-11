from urllib.request import Request, urlopen
import xml.dom.minidom

# Let's construct a request with headers
req = Request('https://msesandbox.cisco.com/api/contextaware/v1/maps/info/DevNetCampus/DevNetBuilding/DevNetZone')
req.add_header('Authorization', 'Basic bGVhcm5pbmc6bGVhcm5pbmc==')

# Actually open the request
response = urlopen(req)

# Read the response into a String
responseString = response.read().decode("utf-8")

# Parse the string into an XML Document Object Model
dom = xml.dom.minidom.parseString(responseString)
xml = dom.toprettyxml()

# Print out the formatted response string
print(xml)

# Get the first object of the document 'Floor'
floor_element = dom.firstChild
if floor_element.hasChildNodes :
    child = floor_element.firstChild
    while child is not None:
        if child.tagName == 'AccessPoint' :
            output = child.tagName + ": " + child.getAttribute('name') + '\t eth: ' + child.getAttribute('ethMacAddress')
            print(output)
        child = child.nextSibling

# Load the XML into a collection of Access Point information
access_points = dom.getElementsByTagName('AccessPoint')
for access_point in access_points:
    ap_name = access_point.getAttribute('name')
    ap_eth_addr = access_point.getAttribute('ethMacAddress')
    ap_ip_addr = access_point.getAttribute('ipAddress')
    print(access_point.tagName + ": " + ap_name + '\t eth: ' + ap_eth_addr + '\t ip: ' + ap_ip_addr)

# Let's close the response we opened
response.close()
