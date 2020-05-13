import string
freq={}
mybook=open("book.txt","rt")
lines=mybook.readlines()
counter = 0
for i in lines:
  a=i.split()
  for j in a: 
    counter += 1
    b=j.strip(string.punctuation)
      if b in freq.keys(): 
        freq[b]= freq[b] + 1
      else:
        freq[b]=1
print(freq)
print(counter)
