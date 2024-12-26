# AbuseIPDB IP Checker

This Python script checks a list of IP addresses against the AbuseIPDB API to determine if any are flagged as malicious. It's designed for bulk IP checking and provides a report based on the abuse confidence score.

## Features
- Check multiple IP addresses at once.
- Get the abuse confidence score for each IP.
- Easy-to-use Python script.

## Requirements
- Python 3.x
- `requests` library (can be installed via `pip`)

## Setup

### 1. Get an API Key from AbuseIPDB

To use this script, you need an API key from [AbuseIPDB](https://www.abuseipdb.com/). Follow these steps:

1. Go to [AbuseIPDB](https://www.abuseipdb.com/).
2. Sign up for a free account (or log in if you already have one).
3. Once logged in, navigate to the **API** section from your dashboard.
4. Copy your **API key** (you will use this in the script).

### 2. Add the API Key to the Script

After obtaining the API key, add it to the `API_KEY` variable in the script:

```python
API_KEY = 'your-api-key-here'

Add the IP List You Want to Check

```python
ips = ["142.250.182.74", "8.8.8.8", "17.253.18.131"]
