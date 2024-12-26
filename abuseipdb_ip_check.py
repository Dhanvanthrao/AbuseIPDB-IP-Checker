import requests

# Your API key from AbuseIPDB
API_KEY = 'api key'

# List of IPs you want to check

ips = ["IP", "IP", "IP"]

# Function to check an IP in AbuseIPDB
def check_ip(ip):
    url = f'https://api.abuseipdb.com/api/v2/check'
    headers = {
        'Key': API_KEY,
        'Accept': 'application/json'
    }
    params = {'ipAddress': ip}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    if data.get('data', {}).get('abuseConfidenceScore', 0) > 50:
        return f"IP {ip} is flagged as malicious."
    return f"IP {ip} is safe."

# Check each IP in the list
for ip in ips:
    print(check_ip(ip))
