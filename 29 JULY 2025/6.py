import re

def punctuations(example):
    ans = re.findall(r"[^\w\s]",example)
    print(ans)

example = input("Enter -- ")
punctuations(example)