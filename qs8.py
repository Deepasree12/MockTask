# method overriding(type of polymorphism)
class new:
  def adding(self,*args):
    return sum(args)
  
a=new()
print(a.adding(2,3))
print(a.adding(2,3,4))

  