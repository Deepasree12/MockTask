# Create a Python class representing a basic stack with push and pop methods.
ls=[]
class stack:
  def push(self,x):
    ls.append(x)
  def pop(self):
    ls.pop()
  def display(self):
    print(ls)

obj=stack()
obj.push(1)
obj.push(3)
obj.pop()
obj.display()
