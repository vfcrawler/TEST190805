import requests_oauthlib
import requests

url = 'https://api.twitter.com/1.1/account/verify_credentials.json'

oauth = requests_oauthlib.OAuth1('YOUR_APP_KEY',
                                 'YOUR_APP_SECRET',
                                 'USER_OAUTH_TOKEN',
                                 'USER_OAUTH_TOKEN_SECRET')

res = requests.get(url,oauth)

print(res.status_code)

