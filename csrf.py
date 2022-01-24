import requests

url = 'https://localhost:8080/login'
getRequest = requests.get(url, verify=False)

# Get Session Key
# Assuming "Set-Cookie:session={{ session_key }}; Path=/; HttpOnly;"
if 'Set-Cookie' in getRequest.headers:
    headText = str(getRequest.headers)
    headLoc = headText.find('session')
    sessionKey = headText[headLoc + 8:headLoc + 119]

# Get CSRF Key
# Assuming "<input type="hidden" name="csrf_token" value="{{ csrf_token() }}"/>"
if 'csrf_token' in getRequest.text:
    csrfText = str(getRequest.text)
    csrfLoc = csrfText.find('csrf')
    csrfKey = csrfText[csrfLoc + 19:csrfLoc + 110]

# Print Keys
print("\nPerforming GET Request on " + url)
print("\nSession Token and CSRF Token are:")
print("\nsession: \"" + sessionKey + "\"")
print("\ncsrfkey: \"" + csrfKey + "\"")
