import re
password=input("Enter the password:")
def validate(password):
    pattern=re.compile("(?=^.{8,}$)(?=.*\d)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$")
    pattern.findall(password)
    if pattern.findall(password)==[]:
        print("The password does not contain an uppercase letteror a digit or a min length of 8 characters")
    else:
        print("The password is strong")
validate(password)