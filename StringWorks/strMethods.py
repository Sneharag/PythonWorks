
# email_id="jhonsmith@gmail.com"

# username,mail=email_id.split(" ")#to split the string using a character(" ",...)

# print(username)

# print(mail)

# print(email_id.startswith("jo"))#to check the text is starting with this character or a group of characters

# print(email_id.endswith("com"))#to check the text is ending with this character or a group of characters

email_id="vipin@yahoo.com"

at_index=email_id.index("@")

username=email_id[:at_index]

rem=email_id[at_index:]

print(username)
print(rem)

# text="/nhello/nworld/n"

# print(text.rstrip("/n"))#remove on right side

# print(text.lstrip("/n"))#remove on left side

# print(text.strip("/n"))#remove in both sides

# print(text.replace("/n"," "))#replace one character with another


# text="helloworld"

# slice=text[0:5]#str_obj[start:end]
# print(slice)

# slice=text[5:]#str_obj[start:]
# print(slice)

# slice=text[:4]#str_obj[:end]
# print(slice)

# slice=text[9:4:-1]
# print(slice)

# slice=text[::-1]
# print(slice)