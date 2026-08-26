import ipaddress
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('ABUSEIPDB_API_KEY')

if api_key is None:
    raise RuntimeError('ABUSEIPDB_API_KEY is not set.')

print(api_key)

ip = '173.234.31.186'

try:
    ipaddress.IPv4Address(ip)
    print(ip)
except ipaddress.AddressValueError:
    print('IP inválido')