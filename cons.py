class token:
  sttable={} 
  def __init__(self,typ,value):
    self.type=typ
    self.value=value
  
  def __str__(self):
    
    return '{typ},{value}'.format(typ=self.type,value=self.value)
    
class varexp():
  
  def eval(self,st):
    if(st in self.sttable):
      return self.sttable[st]
    else:
      self.sttable[st]=0
      return(self.sttable[st])

class consexp:
  def eval(self,st):
    if(st.isalnum()):
      return int(st)
    else:
      return float(st)

class assign:
  var=varexp()
  c=consexp()
  def eval(self,st):
    st1=st.split(':=')
    v=self.var.eval(st1[0])
    c=self.c.eval(st1[1])
    self.sttable[st1[0]]=c
    
class plus:
  c=consexp()
  def eval(self,st):
    st1=st.split('+')
    return (self.c.eval(st1[0])+self.c.eval(st1[1]))

class multiply:
  c=consexp()
  def eval(self,st):
    st1=st.split('*')
    return (self.c.eval(st1[0])*self.c.eval(st1[1]))
 
cons=consexp()
var=varexp()

p=multiply()
a=assign()


a.eval("y:=5")
print(var.eval("y"))

print(p.eval("55*66"))
