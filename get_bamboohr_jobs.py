import requests
import base64

# Your BambooHR subdomain and API key
subdomain = 'your_subdomain'
api_key = 'your_api_key'

# Encode your API Key in base64 as required for Basic Auth
encoded_api_key = base64.b64encode(f"{api_key}:".encode('utf-8')).decode('utf-8')

# The API URL for fetching jobs
jobs_url = f'https://api.bamboohr.com/api/gateway.php/{subdomain}/v1/applicant_tracking/jobs'

# The headers for authorization
headers = {
    'Authorization': f'Basic {encoded_api_key}'
}

# Fetch the list of jobs
response = requests.get(jobs_url, headers=headers)

# Check for a successful response and print the jobs
if response.status_code == 200:
    jobs = response.json()
    for job in jobs:
        print(f"Job ID: {job['id']}, Job Title: {job['title']}")
else:
    print(f"Failed to fetch jobs. Status code: {response.status_code}")
    print('Response:', response.text)

