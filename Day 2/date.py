import re
date=input("Enter the date:")
def validate(date):
    pattern=re.compile("r'\b([0][1-9]|[1][0-2])\/([0][1-9]|[12][0-9]|[3][01])\/[12]\d{3}\b'")
    match=re.findall(pattern,date)
    if match:
        print("The date matches the format 'MM/DD/YYYY'")
    else:
        print("The date doesn't match the format 'MM/DD/YYYY'")
validate(date)
