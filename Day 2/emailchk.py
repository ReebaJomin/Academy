import re
text=input("Enter the email:")
def validate(text):
    pattern=re.compile("\w*.?@(?!yahoo|hotmail)\w*[.][coi][orn][mg]")
    pattern.findall(text)
    if pattern.findall(text)==[]:
        print("The email is invalid")
    else:
        print("The email is valid")
validate(text)
