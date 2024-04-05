thisdict={
    "name":"A",
    "course":"Pg",

}   
mykeys=list(thisdict.keys())
mykeys.sort()
sorteddict={i:thisdict[i] for i in mykeys}
print(sorteddict)