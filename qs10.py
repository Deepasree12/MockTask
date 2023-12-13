'''decorator'''
''''decorator is used to change the beahiviour of a function with out changing its structure'''

def fisrt(func):
  def inner():
    print("sadf")
    func()
  return inner()

@fisrt
def new():
  print("xzcv")
