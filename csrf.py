import requests

url = 'https://localhost:8080/login'
getRequest = requests.get(url, verify=False)

# Get Session Key
if 'Set-Cookie' in getRequest.headers:
    headText = str(getRequest.headers)
    headLoc = headText.find('session')
    sessionKey = headText[headLoc + 8:headLoc + 119]

# Get CSRF Key
if 'csrf-token' in getRequest.text:
    csrfText = str(getRequest.text)
    csrfLoc = csrfText.find('csrf')
    csrfKey = csrfText[csrfLoc + 22:csrfLoc + 113]

# Print Keys
print("\nPerforming GET Request on " + url)
print("\nSession Token and CSRF Token are:")
print("\nsession: \"" + sessionKey + "\"")
print("\ncsrfkey: \"" + csrfKey + "\"")
