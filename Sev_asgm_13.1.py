import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import requests

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

response = requests.get('http://py4e-data.dr-chuck.net/comments_42.xml')
root = ET.fromstring(response.content)

count = root.findall('count')
print(count)

