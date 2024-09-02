
email_id=["sam@gmail.com",
          "smith@gmail.com",
          "jhon@gmail.com",
          "stuart@gmail.com",
          "james@gmail.com"]

f=open("D:\\PythonWorks\\File programs\\email.txt","w")

for email in email_id:

    f.write(email+"\n")