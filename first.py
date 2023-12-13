#qs5: Write a program to copy the contents of one file to another.
x=open('first.txt','r')
data=x.read()
print(x.closed)
x.close()
print(x.closed)
with open('second.txt','a') as f:
  f.write('\n'+data)
