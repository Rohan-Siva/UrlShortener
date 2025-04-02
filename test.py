import pyshorteners

s = pyshorteners.Shortener()
short_url = s.tinyurl.short("https://www.linkedin.com/in/rohan-siva/")
print(short_url)

long_url = s.tinyurl.expand(short_url)
print(long_url)