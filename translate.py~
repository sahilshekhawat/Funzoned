import json
import requests
import urllib
string=raw_input()
langlist=['ar','bg','cs','da','et','fi','fr','it','ko','pt','ru','es']
#langlist=['ar','bg']
b="en"
for i in langlist:

    args = {
            'client_id': 'krngrvr09',#your client id here
            'client_secret': 'bIWuHWwM4mUVjFvbOAMza8t/rbWJaqez9GIjxFuvJZk=',#your azure secret here
            'scope': 'http://api.microsofttranslator.com',
            'grant_type': 'client_credentials'
        }
    oauth_url = 'https://datamarket.accesscontrol.windows.net/v2/OAuth2-13'
    oauth_junk = json.loads(requests.post(oauth_url,data=urllib.urlencode(args)).content)
    translation_args = {
            'text': string,
            'to': i,
            'from': b
            }
    headers={'Authorization': 'Bearer '+oauth_junk['access_token']}
    translation_url = 'http://api.microsofttranslator.com/V2/Ajax.svc/Translate?'
    translation_result = requests.get(translation_url+urllib.urlencode(translation_args),headers=headers)
    string=''.join(''.join((translation_result.content).split("\\")).split('"'))
    print string
    b=i
    

args = {
        'client_id': 'krngrvr09',#your client id here
        'client_secret': 'bIWuHWwM4mUVjFvbOAMza8t/rbWJaqez9GIjxFuvJZk=',#your azure secret here
        'scope': 'http://api.microsofttranslator.com',
        'grant_type': 'client_credentials'
    }
oauth_url = 'https://datamarket.accesscontrol.windows.net/v2/OAuth2-13'
oauth_junk = json.loads(requests.post(oauth_url,data=urllib.urlencode(args)).content)
translation_args = {
        'text': string,
        'to': 'en',
        'from': b
        }
headers={'Authorization': 'Bearer '+oauth_junk['access_token']}
translation_url = 'http://api.microsofttranslator.com/V2/Ajax.svc/Translate?'
translation_result = requests.get(translation_url+urllib.urlencode(translation_args),headers=headers)
print translation_result.content

