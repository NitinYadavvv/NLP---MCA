import re

def mail(example):
    ans = re.findall(r"[A-Za-z0-9][\S]+@gmail.com", example)
    print(ans)

example = input("Enter -- ")
mail(example)
