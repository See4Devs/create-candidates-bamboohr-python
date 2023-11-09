import requests
import json
import base64

# Your BambooHR subdomain and API key
subdomain = 'your_subdomain'
api_key = 'your_api_key'

# Encode your API Key in base64 as required for Basic Auth
encoded_api_key = base64.b64encode(f"{api_key}:".encode('utf-8')).decode('utf-8')

# The API URL for creating a candidate
url = f'https://api.bamboohr.com/api/gateway.php/{subdomain}/v1/applicant_tracking/application'

# The headers for authorization
headers = {
    'Authorization': f'Basic {encoded_api_key}',
    'Content-Type': 'application/json'
}

candidate_data = {
    'firstName': 'Jane',
    'lastName': 'Doe',
    'email': 'jane.doe@email.com',
    'jobId': 'the_job_id_you_obtained',  # Replace with an actual job ID
}

try:
    # Create a Candidate Request
    response = requests.post(url, headers=headers, data=json.dumps(candidate_data))
    
    # Successful POST
    if response.status_code == 200:
        print('Candidate successfully posted to BambooHR.')
    else:
        # Handle specific response codes here, if needed
        print(f'Failed to post candidate. Status code: {response.status_code}')
        print('Response:', response.reason)
except requests.exceptions.RequestException as e:
    # Handle different exceptions such as connection errors, timeouts, etc.
    print('An error occurred: ', e)
