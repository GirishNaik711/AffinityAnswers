import re
import requests



#This functions uses Regex to identify the postal code from an address
def extract_pincode(address):

    regex = r'\b\d{6}\b'
    vp = re.compile(regex)

    matches = re.findall(vp, address)

    return matches[0] if matches else None


#This function uses the extracted pincode and gets its address infromation using the api
def get_pincode_info(pincode):

    api_url = f'http://postalpincode.in/api/pincode/{pincode}'
    response = requests.get(api_url)

    #we'll deduce using the 'Area name' of an address
    if response.status_code == 200:
        data = response.json()
        
        return [data['PostOffice'][i]['Name'] for i in range(len(data['PostOffice']))]
        #There'll be instances where more than 1 name will be present at a single pincode, thus the list comphrehension.
    return None


#the following function checks if the Area we're looking for is present at the specified pincode.
def verify_address(address):

    pincode = extract_pincode(address)

    if pincode:
        
        pincode_info = get_pincode_info(pincode)

        if any(pincode in address for pincode in pincode_info):
            print("Address is correct")
        else:
            print("Address is not correct")
    else:
        print("No pincode found at this address")


c_address = "2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, rugs 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560050"

w_address = "2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560095"
 
verify_address(c_address)
verify_address(w_address)