def eval(st):
  token=[]
  iden=[]
  ope=[]
  num=[]
  token=st.split(' ')
  for i in range(len(token)):
    if token[i].isalpha() :
      iden.append(token[i])
    if token[i].isdigit() :
      num.append(token[i])
    if not token[i].isalpha() and  not token[i].isdigit()  :
      ope.append(token[i])

  print(iden)
  print(ope)
  print(num)

code=[]
code="a = 5;b = 6;a = b + 6;end"
comst=code.split(';')
n=len(comst)
for i in range(n):
  eval(comst[i])
       
  
  
  
