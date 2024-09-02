# print list of words starting with fly

words=["fly","flyin","flyout","flyoff","out","in"]

word="fly"

filter_words=[w for w in words if w.startswith("fly")]

print(filter_words)
