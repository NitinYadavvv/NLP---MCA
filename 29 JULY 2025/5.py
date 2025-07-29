import re

def find_num(example):
    ans = re.findall(r"[0-9]+",example)
    print(ans)

example = input("Enter -- ")
find_num(example)