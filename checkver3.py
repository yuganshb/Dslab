class program:
  def __init__(self,code,sttable):
    self.comst=compoundst(code,sttable)
    self.comst.eval(sttable)

class compoundst:
  def __init__(self,code,sttable):
    self.sts=code.split('\n')
  
  def eval(self,sttable):
    Statements.eval(self.sts,sttable)

class Statements:
  def eval(text,sttable):
    
    i=0
    while(i<len(text)):
    
      if(':=' in text[i]):
        assignst=Assignmentst(text[i][:-1])
        assignst.eval(sttable)
      
      elif('if' in text[i]):
        ifst=Ifst(text,i)
        ifst.eval(sttable)
        i=text.index('fi;')
                
      elif('print' in text[i]):
        printst=Printst(text[i][:-1])
        printst.eval(sttable)
      
      elif('while' in text[i]):
        whilest=Whilest(text,i)
        whilest.eval(sttable)
        i=text.index('done;')
      
      i=i+1
 
#-------------------------------------------------------Statements------------------------------- 
 
class Assignmentst:
  def __init__(self,text):
    self.left=text.split(':=')[0]
    self.right=text.split(':=')[1]
      
  def eval(self,sttable):
    
    self.exp=Expression.eval(self.right,sttable)
    sttable[self.left]=self.exp

class Whilest:
  def __init__(self,text,i):
    self.condst=text[i][text[i].find('(')+1:text[i].find(')')]
    self.text=text
    self.i=i
  def eval(self,sttable):
    self.res=Expression.eval(self.condst,sttable)
    #print(self.text)
    idxdone=self.text.index('done;')
    list1=self.text[self.i+1:idxdone]
    
    while(self.res):
      Statements.eval(list1,sttable)
      self.res=Expression.eval(self.condst,sttable)
    

class Ifst:
  def __init__(self,text,i):
    self.condst=text[i][text[i].find('(')+1:text[i].find(')')]
    self.text=text
    self.i=i  
  def eval(self,sttable):
    self.res=Expression.eval(self.condst,sttable)
    if(self.res):
      idxelse=self.text.index('else')
      list1=self.text[self.i+1:idxelse]
      Statements.eval(list1,sttable)
        
    if(not self.res):

      list1=self.text[self.text.index('else')+1:self.text.index('fi;')]      
      Statements.eval(list1,sttable)

class Printst:
  def __init__(self,text):
    self.pr=text[text.find('(')+1:text.find(')')]
  
  def eval(self,sttable):
    if('"' in self.pr):
      print(self.pr[1:len(self.pr)-1],end=' ')
    else:
      print(Expression.eval(self.pr,sttable),end=' ')

#--------------------------------------------------------Expressions--------------------------------------------

class Constant:
  def eval(text):
    if(text.isalnum()):
      return int(text)
    else:
      return float(text)

class Var:
  def eval(text,sttable):
    if(text in sttable):
      return sttable[text]

#------------------------------------------------------Arithmetic Expression--------------------------------------------1
class Plus():
  def eval(text,sttable):
    idx=text.index('+')  
    return(Expression.eval(text[:idx],sttable)+Expression.eval(text[idx+1:],sttable))

class Minus():
  def eval(text,sttable):
    idx=text.index('-')
    return(Expression.eval(text[:idx],sttable)-Expression.eval(text[idx+1:],sttable))

class Multiply():
  def eval(text,sttable):
    idx=text.index('*')
    return(Expression.eval(text[:idx],sttable)*Expression.eval(text[idx+1:],sttable))

class Divide():
  def eval(text,sttable):
    idx=text.index('/')
    return(Expression.eval(text[:idx],sttable)//Expression.eval(text[idx+1:],sttable))

#--------------------------------------Relational Expression------------------------------------------------------------
class Greater():
  def eval(text,sttable):
    return(Expression.eval(text.split('>')[0],sttable)>Expression.eval(text.split('>')[1],sttable))
    
class Less():
  def eval(text,sttable):
    return(Expression.eval(text.split('<')[0],sttable)<Expression.eval(text.split('<')[1],sttable))

class Greaterequal():
  def eval(text,sttable):
    return(Expression.eval(text.split('>=')[0],sttable)>=Expression.eval(text.split('>=')[1],sttable))

class Lessequal():
  def eval(text,sttable):
    return(Expression.eval(text.split('<=')[0],sttable)<=Expression.eval(text.split('<=')[1],sttable))

class Notequal():
  def eval(text,sttable):
    return(Expression.eval(text.split('!=')[0],sttable)is not Expression.eval(text.split('!=')[1],sttable))

class Equal():
  def eval(text,sttable):
    return(Expression.eval(text.split('=')[0],sttable) is Expression.eval(text.split('=')[1],sttable))

class Expression(Constant):
  def eval(text,sttable):
    
    if(text.isalpha()):
      return Var.eval(text,sttable)
    elif(text.isnumeric()):
      return Constant.eval(text)
    elif('+' in text):
      return Plus.eval(text,sttable)
    elif('-' in text):
      return Minus.eval(text,sttable)
    elif('*' in text):
      return Multiply.eval(text,sttable)
    elif('/' in text):
      return Divide.eval(text,sttable)
    elif('>' in text):
      return Greater.eval(text,sttable)
    elif('<' in text):
      return Less.eval(text,sttable)
    elif('>=' in text):
      return Greaterequal.eval(text,sttable)
    elif('<=' in text):
      return Lessequal.eval(text,sttable)
    elif('!=' in text):
      return Notequal.eval(text,sttable)
    elif('=' in text):
      return Equal.eval(text,sttable)

import sys

filename = sys.argv[1]
file = open(filename)
code = file.read()
file.close()
sttable={}
sttable['ln']='\n'

p=program(code,sttable)
print(sttable)


