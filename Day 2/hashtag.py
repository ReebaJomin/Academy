import re
post=input("Enter a social media post:")
def validate(post):
    pattern=re.compile("#\w*")
    hashtag=pattern.findall(post)
    if hashtag:
        print('The hashtags are:')
        for i in hashtag:
            print(i)
validate(post)

