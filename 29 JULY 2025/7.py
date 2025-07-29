import re

def PAN(example):
    ans = re.findall(r"[A-Z]{5}[0-9]{4}[A-Z]{1}",example)
    print(ans)

example = input("Enter -- ")
PAN(example)