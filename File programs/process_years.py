
f_read=open("D:\\PythonWorks\\File programs\\years.txt","r")

f_century=open("D:\\PythonWorks\\File programs\\century_year.txt","w")

f_non_century=open("D:\\PythonWorks\\File programs\\non_century.txt","w")

for year in f_read:

    y=int(year.rstrip("\n"))
    
    if y%100==0:

        f_century.write(str(y)+"\n")

    else:

        f_non_century.write(str(y)+"\n")
