#Unit=3: List,Tuple,Dictionary
#1.List[]:

thislist=["PASS","FAIL","ATKT"]
thislist.append("COVID PASS")
thislist.remove("FAIL")
print(thislist)
for i in thislist:
    print(i)
print(len(thislist))
print(type(thislist))
thislist[0]="FAIL"
print(thislist[0])
i=0
while i<len(thislist):
    print(thislist[i])
    i=i+1
    