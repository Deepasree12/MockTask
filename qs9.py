
# method overriding...(2 classes with smae function and same arguments)

class New:
  def first(self,x,y):
    return x+y
class child(New):
  def first(self,x,y):
    return x-y
    
a=child()
print(a.first(10,20))
