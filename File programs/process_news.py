

f=open("D:\\PythonWorks\\File programs\\news.txt","r")

word_lst=[w for line in f for w in line.rstrip("\n").split(" ") if w != ""]

word_count={w:word_lst.count(w) for w in word_lst}

print(word_count)

sort=sorted(word_count,key=lambda key:word_count.get(key),reverse=True)

print(sort[0])
