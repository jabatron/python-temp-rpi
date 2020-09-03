import requests

ip_r = requests.get('https://ifconfig.me/ip/')

print (ip_r.text)
# aquí tengo la ip

API_KEY = 'f2833266890f4c94a1be8f5af7157cb6'
IP = ip_r.text  
LANG = 'sp'

URL = 'https://api.ipgeolocation.io/astronomy?apiKey=' + API_KEY + '&ip=' + IP + '&lang=' + LANG

r = requests.get(URL)

print (r.text)
data = r.json()

print (data["sunrise"])
print (data["sunset"])
print (data["current_time"])

