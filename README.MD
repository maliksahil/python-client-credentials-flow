# AAD Python Client Credentials flow

This code example demonstrates how to use Python to call a service registered in Azure AD using the client credential flow (a.ka. acting as a daemon)

## Here is how to get this setup,
1. Register an app in AAD, any redirect URI is fine
2. Create a client secret
3. Under expose an api, create an appid uri, example https://sahilmalikgmail.onmicrosoft.com/pythonservice
4. Host a service at a URL with the above matching info (you wont need client secret on the service).
5. Update this client to use the client secret, client id, and scope like this --> https://sahilmalikgmail.onmicrosoft.com/pythonservice/.default .. you can choose to create more scopes if you wish.
6. That's it! Run the service, run the client, party!