import re
number=input("Enter the phone-number:")
def validate(number):
    pattern=re.compile("\(\d{3}\)\d{3}-\d{4}")
    pattern.findall(number)
    if pattern.findall(number)==[]:
        print("The phone-no is invalid")
    else:
        print("The phone-no is valid")
validate(number)