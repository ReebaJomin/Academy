import re
url=input("Enter the URL to extract domain:")
def validate(url):
    pattern=re.compile("https?://(www\.)?([^/]+)")
    match=re.search(pattern,url)
    if match:
        domain=match.group(2)
        print("Domain:",domain)
validate(url)