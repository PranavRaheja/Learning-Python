import requests
import  json
print("\n")
def pin_to_state():
    endp = "https://api.postalpincode.in/pincode/"
    print("hello!\n")
    pincode = str(input("enter the pincode: "))
    response = requests.get(endp+pincode)
    info = json.loads (response.text)
    divis=(info[0]["PostOffice"][0]["Division"])
    print("Your city is",divis)
    
    def s_toweather():
        key = "2b1e8e290ff745918bb134537240301"
        base_url = "http://api.weatherapi.com/v1"
        compl_url = base_url +"/current.json?key="+key+"&q="+divis
        #print(compl_url)
        gets = ((requests.get(compl_url)))
        gets_stored = json.loads(gets.text)  
        temp_c = gets_stored['current']['temp_c']
        temp_f = gets_stored['current']['temp_f']
        lati = gets_stored['location']['lat']
        longi = gets_stored['location']['lon']
        print(f"Temperature in {divis}: {temp_c} C or {temp_f}F")
        print(f"Your coordinates are {lati} {longi}")
        #print("temp is as follows:\n In celsius",gets_stored[260:265],"\n In Fahrenheit :",gets_stored[275:279])
    s_toweather()
    

pin_to_state()



















#code process
#def disp_coord():

   
# def state_to_weather():
#     resp = "http://api.weatherapi.com/v1/current.json?key=2b1e8e290ff745918bb134537240301&q=Paris" 
#     base_url = http://api.weatherapi.com/v1
#     resp2= requests.get(resp)
#     print(resp2)
#     answer = resp2.text
#     print(answer)
   
# pin_to_state()
# base_url = "http://api.weatherapi.com/current.json"
# comp_url ="http://api.weatherapi.com/current.json?key=2b1e8e290ff745918bb134537240301&q=divis"
# #comp_url = base_url +key+"&q="+divis
# print(requests.get(comp_url))
# '''reqs = requests.get(comp_url)
# answer = reqs.json()
# print(answer)
# print("hi")





