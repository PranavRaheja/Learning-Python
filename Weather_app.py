import requests
import pandas as pd
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
        key = "c2e6251262d842f78d9151941242601"
        base_url = "http://api.weatherapi.com/v1"
        compl_url = base_url +"/current.json?key="+key+"&q="+divis               
        gets = ((requests.get(compl_url)))
        gets_stored = json.loads(gets.text)  
        temp_c = gets_stored['current']['temp_c']
        temp_f = gets_stored['current']['temp_f']
        lati = gets_stored['location']['lat']
        longi = gets_stored['location']['lon']
        print(f"Temperature in {divis}: {temp_c} C or {temp_f}F")
        print(f"Your coordinates are {lati} {longi}")
        #print("temp is as follows:\n In celsius",gets_stored[260:265],"\n In Fahrenheit :",gets_stored[275:279])
        
        #Load existing data from excel file if it exists
        excel_file_path = 'weather_data.xlsx'
        try:
            existing_data = pd.read_excel(excel_file_path)
        except(FileNotFoundError):
            existing_data = pd.DataFrame()
            
        new_data = {
            'Pincode':[pincode],
            'City':[divis],
            'Temp(c)':[temp_c],
            'Temp(f)':[temp_f],
            'Latitude':[lati],
            'Longitude':[longi]
            
            
        }
        comb_data = pd.concat([existing_data,pd.DataFrame(new_data)],ignore_index=True)
        
        #save combined to excel
        comb_data.to_excel(excel_file_path,index=False)
        
        print(f"Data has been stored in the excel file : {excel_file_path}")
              
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





