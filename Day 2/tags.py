import re
html=input("Enter the string:")
def validate(html):
    pattern=re.compile("[<]\/?\w*[>]")
    new_text=re.sub(pattern,"",html)
    print(f'The string without html tags:{new_text}')
validate(html)

#<(?:"[^"]*"[''']*|'[^']*'[''']*|[^'''>])+>