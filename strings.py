vow=0
const=0
str=input("Enter the string to analyze:")
for i in str:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        vow+=1
    elif i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        vow+=1
    elif i!=" ":
        const+=1
print(f'The string contains {vow} vowels and {const} consonants')