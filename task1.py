import string
mybook=open("book.txt","r")
lines=mybook.readlines()
for i in lines:
  a=i.split(' ')
  for j in a:
    b=j.strip(string.punctuation)
    print(b.lower())
