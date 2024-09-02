
lst=[10,20,10,11,12,11,12,13,14]

number_count={num:lst.count(num) for num in lst}
print(number_count)

text="hello hai hello hai hello"

words=text.split(" ")
word_count={w:words.count(w) for w in words}
print(word_count)