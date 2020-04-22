import requests
import xml.dom.minidom
# We need to import the JSON library just to handle our request to the APIC for login
import json


# We need to log in to the APIC and gather a token, before we can access any data
# Let's construct a request with a body

# We'll need to disable certificate warnings
requests.packages.urllib3.disable_warnings()

# We need to have a body of data consisting of a username and password to gather a cookie from APIC

encoded_body = json.dumps({
	        "aaaUser": {
		        "attributes": {
			        "name": "admin",
			        "pwd": "ciscopsdt"
                 }
            }
})

# Now lets make the request and store the data
resp = requests.post("https://sandboxapicdc.cisco.com/api/aaaLogin.json", data=encoded_body, verify=False)

print(resp.status_code)
print(resp.cookies["APIC-cookie"])
header = {"Cookie": "APIC-cookie=" +  resp.cookies["APIC-cookie"]}

tenants = requests.get("https://sandboxapicdc.cisco.com/api/node/class/fvTenant.xml", headers=header, verify=False)

print(tenants.text)