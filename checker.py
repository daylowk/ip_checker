import ipaddress
import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('ABUSEIPDB_API_KEY')

if api_key is None:
    raise RuntimeError('ABUSEIPDB_API_KEY is not set.')

ip = '10.0.0.255'

try:
    ipaddress.IPv4Address(ip)
    print(ip)
except ipaddress.AddressValueError:
    print('IP inválido')

url = 'https://api.abuseipdb.com/api/v2/check'

headers = {
    'key': api_key,
    'Accept': 'application/json'
}

params = {
    'ipAddress': ip
}

response = requests.get(url, headers=headers, params=params)

print(response.status_code)
print(response.json())