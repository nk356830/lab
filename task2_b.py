from collections import Counter
import string
nl=[]
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
Counter=Counter(freq)
most_occur=Counter.most_common(20)
print(most_occur)