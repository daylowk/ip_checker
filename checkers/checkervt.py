import os
import json

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('VIRUSTOTAL_API_KEY')

def check_api(ip):
    url = f'https://www.virustotal.com/api/v3/ip_addresses/{ip}'

    headers = {
        'accept': 'application/json',
        'x-apikey': api_key
    }

    try:
        response = requests.get(
            url=url,
            headers=headers,
            timeout=10
            )

        response.raise_for_status()
    except requests.RequestException as error:
        print(f'VirusTotal API failed: {error}')
        return None

    return response.json()['data']

def text_output(data):
    print('—————————————————————————————————————————')
    print('VirusTotal')
    print('———————————————————')
    print()
    print(f'IP: {data['id']}')
    print(f'Country: {data['attributes']['country']}')
    print(f'ASN: {data['attributes']['asn']}')
    print(f'AS Owner: {data['attributes']['as_owner']}')
    print(f'Network: {data['attributes']['network']}')
    print(f'RIR: {data['attributes']['regional_internet_registry']}')
    print()
    print(f'Community Reputation: {data['attributes']['reputation']}')
    print()
    print('Analysis:')
    print(f'\tMalicious: {data['attributes']['last_analysis_stats']['malicious']}')
    print(f'\tSuspicious: {data['attributes']['last_analysis_stats']['suspicious']}')
    print(f'\tHarmless: {data['attributes']['last_analysis_stats']['harmless']}')
    print(f'\tUndetected: {data['attributes']['last_analysis_stats']['undetected']}')
    print(f'\tTimeout: {data['attributes']['last_analysis_stats']['timeout']}')
    print('—————————————————————————————————————————')

def check_ip(ip, output):
    data = check_api(ip)

    if data is not None:
        if output == 'text':
            text_output(data)
        