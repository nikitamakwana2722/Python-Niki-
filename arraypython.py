#Array in Python:

cars=["Nano","Nanoxl"]
cars[0]="xyz"
print(cars[0])
print(len(cars))
cars.append("Honda")  #for new Add
cars.append("Honda1") #for new Add
cars.pop(0)           #for remove
cars.remove("Honda1") #for remove
for x in cars:
    print(x)