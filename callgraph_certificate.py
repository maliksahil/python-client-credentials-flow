from OpenSSL.crypto import load_certificate, FILETYPE_PEM
from JwtAssertionCreator import JwtAssertionCreator

import requests, json

client_id = 'clientid'
tenantname = 'tenantname'

graph_api_url = "https://graph.microsoft.com/v1.0/users"
token_endpoint = "https://login.microsoftonline.com/" + tenantname + "/oauth2/v2.0/token"
scope = "https://graph.microsoft.com/.default"

with open('key_unencrypted.pem', 'rb') as f:
   private_key = f.read()

cert_file_string = open("cert.pem", "rb").read()
cert = load_certificate(FILETYPE_PEM, cert_file_string)
sha1_thumbprint = cert.digest("sha1").decode("utf-8").replace(":","")

client_assertion=JwtAssertionCreator(
                        private_key,
                        algorithm="RS256",
                        sha1_thumbprint=sha1_thumbprint
                    ).create_normal_assertion(
                        audience=token_endpoint,
                        issuer=client_id,
                    ).decode("utf-8") 

data = "client_id=" + client_id + "&scope=" + scope + "&client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer" + "&grant_type=client_credentials" + "&client_assertion=" + client_assertion

access_token_response = requests.post(
    token_endpoint, 
    data=data)

print(access_token_response.headers)
print(access_token_response.text)

tokens = json.loads(access_token_response.text)

print ("access token: " + tokens['access_token'])

api_call_headers = {'Authorization': 'Bearer ' + tokens['access_token']}
api_call_response = requests.get(graph_api_url, headers=api_call_headers, verify=False)

print (api_call_response.text)