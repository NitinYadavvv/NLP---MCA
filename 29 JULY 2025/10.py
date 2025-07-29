import re

def capital_letter(example):
    ans = re.findall(r"[A-Z][\S]+", example)
    print(ans)

example = input("Enter -- ")
capital_letter(example)
