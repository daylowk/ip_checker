import argparse
import ipaddress
import os

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('ABUSEIPDB_API_KEY')

if api_key is None:
    raise RuntimeError('ABUSEIPDB_API_KEY is not set.')

LOW_THRESHOLD = 25
MEDIUM_THRESHOLD = 50
HIGH_THRESHOLD = 75

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

def risk_score(score):
    if score < LOW_THRESHOLD:
        return 'Low'
    elif score < MEDIUM_THRESHOLD:
        return 'Medium'
    elif score < HIGH_THRESHOLD:
        return 'High'
    else:
        return 'Critical'

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

    if response is not None:
        data = response.json()['data']
        print(f'IP: {data['ipAddress']}')
        print(f'Country: {data['countryCode']}')
        print(f'ISP: {data['isp']}')
        print(f'Host Name: {data['hostnames']}')
        print(f'Domain: {data['domain']}')
        print()
        print(f'Abuse Confidence Score: {data['abuseConfidenceScore']}')
        print(f'Total Reports: {data['totalReports']}')
        print(f'Distinct Users Reports: {data['numDistinctUsers']}')
        print(f'Last Report: {data['lastReportedAt']}')
        print()
        print(f'Risk: {risk_score(data['abuseConfidenceScore'])}')
except ipaddress.AddressValueError:
    print('IP inválido')
