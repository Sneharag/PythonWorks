
from re import fullmatch

f=open("D:\\PythonWorks\\regularExpression\\domain.txt")

# pattern=".*.com"

pattern="[\\w\\W]+\\.com"

for line in f:

    domain=line.rstrip("\n")

    matcher=fullmatch(pattern,domain)

    if matcher!=None:

        print(domain)