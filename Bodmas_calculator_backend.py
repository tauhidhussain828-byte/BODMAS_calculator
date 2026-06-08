operators=['+','-','*','/']
def calculator(a):
     def identification(a):#defining the funtion to gather the number from expression and print it in bs
           for i in a:
                if i.isdigit() or i in operators or i in "()":#checks if there is digit or not
                     pass
                else:
                    print("error boom!")  
                    return False  
           return True  
     def bracket_solver(a):
           while '(' in a:
            bracketopen=a.rfind('(')
            bracketclose=a.find(')',bracketopen)
            innerexpression=a[bracketopen+1 : bracketclose]
            ms,op=storing(innerexpression)
            value=evaluation(ms,op)
            a=a[:bracketopen]+str(value)+a[bracketclose+1:]
           return a
     def storing(a):
          ms=[]#main slot
          bs=[]#buffer slot
          op=[]#operator slot
          for i in a:
               if i.isdigit():
                    bs.append(i)
               elif i in operators:
                    op.append(i)
                    b = int("".join(bs))
                    ms.append(b)
                    bs.clear()
          if bs:
               b = int("".join(bs))
               ms.append(b)
               bs.clear()
          return ms,op
     def evaluation(ms,op):
                  i = 0
                  while i < len(op):
                        if op[i] == '*':
                              ms[i] = ms[i] * ms[i+1]
                              del ms[i+1]
                              del op[i]
                        elif op[i] == '/':
                              ms[i] = ms[i] / ms[i+1]
                              del ms[i+1]
                              del op[i]
                        else:
                             i += 1  
                  i=0
                  while i < len(op):
                        if op[i] == '+':
                              ms[i] = ms[i] + ms[i+1]
                              del ms[i+1]
                              del op[i]
                        elif op[i] == '-':
                              ms[i] = ms[i] - ms[i+1]
                              del ms[i+1]
                              del op[i]
                  return ms[0]
     if not identification(a):
           return
     a=bracket_solver(a)
     ms,op=storing(a)
     result=evaluation(ms,op)
     return result
