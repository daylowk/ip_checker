# IP Checker

This is a command-line tool for checking the reputation of IP addresses using AbuseIPDB and VirusTotal.

## Features

- Check IPv4 addresses from the command line.
- Query AbuseIPDB for IP reputation information.
- Query VirusTotal for IP reputation and network information.
- Query both APIs at the same time.
- Display results in human-readable text or JSON.

## APIs
### AbuseIPDB

The AbuseIPDB integration provides information such as:
- IP address
- Country
- ISP
- Hostnames
- Domain
- Abuse Confidence Score
- Number of reports
- Number of distinct reporters
- Last reported time
- Risk classification

### VirusTotal

The VirusTotal integration provides information such as:
- IP address
- Country
- ASN
- AS owner
- Network
- Regional Internet Registry (RIR)
- Community reputation
- Malicious detections
- Suspicious detections
- Harmless detections
- Undetected detections
- Timeout detections

The information given by each API might not match with the other.

## Requirements

- Python 3.x
- An AbuseIPDB API key
- A VirusTotal API key

### To get the keys

AbuseIPDB: Log in to [abuseipdb.com](https://www.abuseipdb.com/login), then go to [My API](https://www.abuseipdb.com/account/api/keys) and create your API key.

VirusTotal: Log in to [VirusTotal](https://www.virustotal.com/gui/sign-in) and your key is going to be in [API Key](https://www.virustotal.com/gui/my-apikey).

## Installation

Clone the repository:
```bash
git clone https://github.com/daylowk/ip_checker
cd ip_checker
```
Install the dependencies:
```bash
pip install -r requirements.txt
```

## Configuration 

The API keys are loaded from enviroment variables using ```python-dotenv```.

Create a ```.env``` file in the project root:
```
ABUSEIPDB_API_KEY=your_abuseipdb_api_key
VIRUSTOTAL_API_KEY=your_virustotal_api_key
```
## Usage

The basic syntax is:
```bash
python3 checker.py <IP>
```
You can select a specific API:
```bash
python3 checker.py --api <VirusTotal, AbuseIPDB, All> <IP>
```
You can select the output (the JSON output preserves the original data given by the API):
```bash
python3 checker.py -a VirusTotal --output <text or json> <IP>
```
You can also save the output into a file:
```bash
python3 checker.py -a AbuseIPDB -o json <IP> > <file>
```

Example:
```bash
python3 checker.py 8.8.8.8
```

<img width="525" height="728" alt="image" src="https://github.com/user-attachments/assets/256743b3-605c-45a3-bdc1-bae97b5392fe" />

## Data Sources

- [AbuseIPDB](https://www.abuseipdb.com/)
- [VirusTotal](https://www.virustotal.com/)
