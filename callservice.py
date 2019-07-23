import requests, json

token_url = "https://login.microsoftonline.com/sahilmalikgmail.onmicrosoft.com/oauth2/v2.0/token"
test_api_url = "api_url"

client_id = 'clientid'
client_secret = 'clientsecret'
scope = 'scope'

data = "client_id=" + client_id + "&scope=" + scope + "&client_secret=" + client_secret + "&grant_type=client_credentials"

access_token_response = requests.post(
    token_url, 
    data=data, 
    verify=False, 
    allow_redirects=False, auth=(client_id, client_secret))

print(access_token_response.headers)
print(access_token_response.text)

tokens = json.loads(access_token_response.text)

print ("access token: " + tokens['access_token'])

api_call_headers = {'Authorization': 'Bearer ' + tokens['access_token']}
api_call_response = requests.get(test_api_url, headers=api_call_headers, verify=False)

print (api_call_response.text)