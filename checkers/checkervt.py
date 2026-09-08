import os
import ipaddress
import json

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('VIRUSTOTAL_API_KEY')

ip = '185.136.15.12'

url = f'https://www.virustotal.com/api/v3/ip_addresses/{ip}'
headers = {
    'accept': 'application/json',
    'x-apikey': api_key
}

response = requests.get(url=url, headers=headers)

response = json.dumps(response.json(), indent=4)
print(response)