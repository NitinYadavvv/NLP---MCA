import re

def mention(example):
    ans = re.findall(r"@[A-Z a-z 0-9][\S]+",example)
    print(ans)

example = input("Enter -- ")
mention(example)