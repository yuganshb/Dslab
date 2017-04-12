import sys

filename = sys.argv[1]
file = open(filename)
code = file.read()
file.close()

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
              
      #elif('while' in self.sts[i]):
        #self.whilest=Whilest(self.sts[i])
      
      #elif('done' in self.sts[i]):
        #self.donest=Donest(self.sts[i])
      
      i=i+1       
     
class program:
  def __init__(self,code,sttable):
    self.comst=compoundst(code,sttable)
    self.comst.eval(sttable)


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
    
class Greater(Expression):
  def eval(text,sttable):
    return(Expression.eval(text.split('>')[0],sttable)>Expression.eval(text.split('>')[1],sttable))
    
class Less(Expression):
  def eval(text,sttable):
    return(Expression.eval(text.split('<')[0],sttable)<Expression.eval(text.split('<')[1],sttable))

class Greaterequal(Expression):
  def eval(text,sttable):
    return(Expression.eval(text.split('>=')[0],sttable)>=Expression.eval(text.split('>=')[1],sttable))

class Lessequal(Expression):
  def eval(text,sttable):
    return(Expression.eval(text.split('<=')[0],sttable)<=Expression.eval(text.split('<=')[1],sttable))

class Notequal(Expression):
  def eval(text,sttable):
    return(Expression.eval(text.split('!=')[0],sttable)!=Expression.eval(text.split('!=')[1],sttable))

class Equal(Expression):
  def eval(text,sttable):
    return(Expression.eval(text.split('=')[0],sttable) is Expression.eval(text.split('=')[1],sttable))

class Plus(Expression):
  def eval(text,sttable):
    return(Expression.eval(text.split('+')[0],sttable)+Expression.eval(text.split('+')[1],sttable))
    
class Minus(Expression):
  def eval(text,sttable):
    return(Expression.eval(text.split('-')[0],sttable)-Expression.eval(text.split('-')[1],sttable))

class Multiply(Expression):
  def eval(text,sttable):
    return(Expression.eval(text.split('*')[0],sttable)*Expression.eval(text.split('*')[1],sttable))
    

class Printst:
  def __init__(self,text):
    self.pr=text[text.find('(')+1:text.find(')')]
  
  def eval(self,sttable):
    if('"' in self.pr):
      print(self.pr[1:len(self.pr)-1])
    else:
      print(sttable[self.pr])



class Ifst:
  def __init__(self,text,i):
    self.condst=text[i][text[i].find('(')+1:text[i].find(')')]
    self.text=text
    self.i=i  
  def eval(self,sttable):
    self.res=Expression.eval(self.condst,sttable)
    if(self.res):
      list1=self.text[self.i+1:self.text.index('else')]
      Statements.eval(list1,sttable)
        
    if(not self.res):

      #list1=self.text[self.text.index('else')+1:self.text.index('fi;')]      
      Statements.eval(list1,sttable)
      


class Assignmentst:
  def __init__(self,text):
    self.left=text.split(':=')[0]
    self.right=text.split(':=')[1]
      
  def eval(self,sttable):
    
    self.exp=Expression.eval(self.right,sttable)
    sttable[self.left]=self.exp
               

sttable={}
p=program(code,sttable)
#print(code)
print(sttable)

