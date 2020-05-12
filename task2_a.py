
mybook=open("book.txt","rt")
lines=mybook.readlines()
counter = 0
for i in lines:
  a=i.split()
  for j in a:
    counter += 1
print(counter)
