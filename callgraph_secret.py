import requests, json

client_id = 'clientid'
client_secret = 'clientsecret'
tenantname = 'tenantname'

graph_api_url = "https://graph.microsoft.com/v1.0/users"
token_endpoint = "https://login.microsoftonline.com/" + tenantname + "/oauth2/v2.0/token"
scope = 'https://graph.microsoft.com/.default'

data = "client_id=" + client_id + "&scope=" + scope + "&client_secret=" + client_secret + "&grant_type=client_credentials"

access_token_response = requests.post(
    token_endpoint, 
    data=data, 
    verify=False, 
    allow_redirects=False, auth=(client_id, client_secret))

print(access_token_response.headers)
print(access_token_response.text)

tokens = json.loads(access_token_response.text)

print ("access token: " + tokens['access_token'])

api_call_headers = {'Authorization': 'Bearer ' + tokens['access_token']}
api_call_response = requests.get(graph_api_url, headers=api_call_headers, verify=False)

print (api_call_response.text)