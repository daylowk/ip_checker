import os
import json

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('ABUSEIPDB_API_KEY')

if api_key is None:
    raise RuntimeError('ABUSEIPDB_API_KEY is not set.')

LOW_THRESHOLD = 25
MEDIUM_THRESHOLD = 50
HIGH_THRESHOLD = 75

def check_api(ip):
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

    return response.json()['data']

def risk_score(score):
    if score < LOW_THRESHOLD:
        return 'Low'
    elif score < MEDIUM_THRESHOLD:
        return 'Medium'
    elif score < HIGH_THRESHOLD:
        return 'High'
    else:
        return 'Critical'

def text_output(data):
    print('—————————————————————————————————————————')
    print('AbuseIPDB')
    print('———————————————————')
    print()
    print(f'IP: {data['ipAddress']}')
    print(f'Country: {data['countryCode']}')
    print(f'ISP: {data['isp']}')
    hostnames = data['hostnames']
    if hostnames:
        print(f'Host Name: {', '.join(hostnames)}')
    else:
        print('Host Name: None')
    print(f'Domain: {data['domain']}')
    print()
    print(f'Abuse Confidence Score: {data['abuseConfidenceScore']}')
    print(f'Total Reports: {data['totalReports']}')
    print(f'Distinct Users Reports: {data['numDistinctUsers']}')
    print(f'Last Report: {data['lastReportedAt']}')
    print()
    print(f'Risk: {risk_score(data['abuseConfidenceScore'])}')
    print('—————————————————————————————————————————')

def json_output(data):
    output = {
        'data': data,
        'analysis': {
            'risk': risk_score(data['abuseConfidenceScore'])
        }
    }

    print(json.dumps(output, indent=4))

def check_ip(ip, output):
    data = check_api(ip)

    if data is not None:
        if output == 'text':
            text_output(data)
        else:
            json_output(data)
