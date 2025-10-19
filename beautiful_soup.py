import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup("a")
for tag in tags:
    print("Tag ", tag)
    print("Url: ", tag.get("href"))
    print("Attributes: ", tag.attrs)