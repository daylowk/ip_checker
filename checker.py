import argparse
import ipaddress
from checkers.checkeripdb import check_ip as abuse_check
'''from checkers.checkervt import check_ip as vt_check'''

parser = argparse.ArgumentParser()
parser.add_argument(
    'ip',
    metavar='IP',
    help='IP address used for the consultation.'
)
parser.add_argument(
    '-o',
    '--output',
    choices=['text','json'],
    default='text',
    help='Which output to return.'
)
parser.add_argument(
    '-a',
    '--api',
    choices=['AbuseIPDB', 'VirusTotal', 'All'],
    default='All',
    help='Which API(s) to consult.'
)

args = parser.parse_args()

ip = args.ip

try:
    ipaddress.IPv4Address(ip)
    if args.api in ('AbuseIPDB', 'All'):
        abuse_check(ip, args.output)
    
except ipaddress.AddressValueError:
    print('IP inválido.')
