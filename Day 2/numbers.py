import re
num=input("Enter the text:")
def validate(num):
    pattern=re.compile("\d+")
    numbers=pattern.findall(num)
    if numbers:
        print('The numbers are:')
        for i in numbers:
            print(i)
validate(num)