import os, os.path, json, requests

from api_key import PROXYCURL_API_KEY
 
def scrapeLinkedIn(name='eden-marco'):
    
    os.environ['PROXYCURL_API_KEY'] = PROXYCURL_API_KEY
 
    fname = f"{name}.json"
    if os.path.isfile(fname):
	    with open(fname, 'r') as fh:
		    str = fh.read()
		    return json.loads(str)
 
    proxyCurlUrl = 'https://nubela.co/proxycurl/api/v2/linkedin'
    linkedInUrl = f"https://www.linkedin.com/in/{name}"
    hHeaders = {
		'Authorization': f"Bearer {PROXYCURL_API_KEY}"
		}
    hParams = {
		'url': linkedInUrl,  # will work with just this
 
		'fallback_to_cache': 'on-error',
		'use_cache': 'if-present',
		'skills': 'include',
		'inferred_salary': 'include',
		'personal_email': 'include',
		'personal_contact_number': 'include',
		'twitter_profile_id': 'include',
		'facebook_profile_id': 'include',
		'github_profile_id': 'include',
		'extra': 'include',
		}
 
	# --- resp has these fields:
	#        status_code - should be 200, otherwise an error occurred
	#        headers - a hash of header name/header value
	#        encoding - should be 'utf-8'
	#        text - the text of the response, should be a JSON string
	#        json() - interprets text as JSON, returns a data structure
 
    resp = requests.get(proxyCurlUrl,
			params=hParams,
			headers=hHeaders)
    assert resp.status_code == 200, "Bad status"
    with open(fname, 'w') as fh:
	    fh.write(resp.text)
    return resp.json()


 
data = scrapeLinkedIn()
print(data)
    