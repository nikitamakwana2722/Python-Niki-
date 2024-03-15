0#Control Structure:break,continue,pass
# 1.Break:

for i in range (1,6):
    if (i==3):
        break
    else:
        print(i)
        
#2.Continue:

for i in range (1,6):
    if (i==3):
        continue
    else:
        print(i)
        
#3.Pass:

for x in range(1,10):
    print(x)
    if x==5:
        pass   #placeholder for future code.      