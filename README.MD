# AAD Python Client Credentials flow

This code example demonstrates how to use Python to call a service registered in Azure AD using the client credential flow (a.ka. acting as a daemon)

## Here is how to get this setup,
1. Register an app in AAD, no redirect URI etc.
2. Create a client secret
3. Grant an application permission to Graph, such as User.Read, remember to grant consent also.

### For client credential flow using a client secret
1. Create a client secret
2. Update the callgraph_secret.py file's following lines
```
client_id = 'clientid'
client_secret = 'clientsecret'
tenantname = 'tenantname'
```
3. Run the file, verify that you get an access token and you can call Graph.

## For client credential flow using a certificate
1. Generate a cert
```openssl req -x509 -days 3650 -newkey rsa:2048 -keyout key.pem -out cert.pem```
2. Create an unprotected private key (it is possible to do this with a protected key also)
```openssl rsa -in key.pem -out key_unencrypted.pem```
3. Update the callgraph_certificate.py file's following lines
```
client_id = 'clientid'
tenantname = 'tenantname'
```
4. Run the file, verify that you get an access token and you can call Graph.
