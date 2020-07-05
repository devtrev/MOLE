import urllib.request, urllib.error
from unittest import TestCase

print("Docker is magic!")

assert True

urlList = dict({
'Google': 'http://www.google.com', 
'Google_bad': 'http://www.google.com/aaaa',
'Test_bad': 'https://www.hkkrdsdoociffs.com',
'Google_https': 'https://www.google.com' 
}) 

for key, url in urlList.items():
    try:
        conn = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
    	# Return code error (e.g. 200, 404, 501, ...)
    	print(key + ' : {}'.format(e.code))
    except urllib.error.URLError as e:
    	# Not an HTTP-specific error (e.g. connection refused)
    	# ...
    	print(key + ' : {}'.format(e.reason))    
    else :
    	# Not an HTTP-specific error (e.g. connection refused)
    	# ...
        print(key + ' : 200')

assert True