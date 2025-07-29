import re

def PAN(example):
    ans = re.findall(r"91[6-9]\d{9}",example)
    print(ans)

example = input("Enter -- ")
PAN(example)