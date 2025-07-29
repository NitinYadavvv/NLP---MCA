import re

def hash(example):
    ans = re.findall(r"#[A-Z a-z 0-9][\S]+",example)
    print(ans)

example = input("Enter -- ")
hash(example)