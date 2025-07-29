import re

def url(example):
    ans = re.findall(r"https://[\S]+", example)
    print(ans)

example = input("Enter -- ")
url(example)
