import argparse
import ipaddress
import os

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('ABUSEIPDB_API_KEY')

if api_key is None:
    raise RuntimeError('ABUSEIPDB_API_KEY is not set.')

def check_ip(ip):
    url = 'https://api.abuseipdb.com/api/v2/check'

    headers = {
    'key': api_key,
    'Accept': 'application/json'
    }

    params = {
    'ipAddress': ip
    }

    try:
        response = requests.get(url=url,
            headers=headers,
            params=params,
            timeout=10
            )

        response.raise_for_status()
    except requests.RequestException as error:
        print(f'API request failed: {error}')
        return None

    return response

parser = argparse.ArgumentParser()
parser.add_argument(
    'ip',
    metavar='IP',
    help='IP address used for the consultation.'
)

args = parser.parse_args()

ip = args.ip

try:
    ipaddress.IPv4Address(ip)
    response = check_ip(ip)
    print(ip)
    print(response.status_code)
    print(response.json())
except ipaddress.AddressValueError:
    print('IP inválido')
