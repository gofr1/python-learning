import urllib.request

web_url = urllib.request.urlopen("https://google.com")
print("Result code:", web_url.getcode())

data = web_url.read()
print(data)