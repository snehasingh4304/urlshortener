import pyshorteners
long_url=input("enter the URL to shorten:")
type_tiny=pyshorteners.Shortener()
short_url=type_tiny.tinyurl.short(long_url)
print("the shortened URL is:"+ short_url)
