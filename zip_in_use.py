a = [1,2,3,4,5]
b = ['Debjit', 'Anirban', 'Shreya', 'Pratik', 'Fahaad']
c = [4, 1, 2, 11, 56]

#zipping
for i,name,roll in zip(a,b,c):
    print(i,name,roll)
print(list(zip(a,b,c)))
for position, name, roll in list(zip(a,b,c)):
    if roll >= 2 and roll < 7:
        print(name, position)
    else:
        print(name)
        
## zipping        
map = zip(a,b,c)
map = list(map)
print('Mapped Values :- \n' , map)

## Unzipping
pos, names , roll = zip(*map)
print('Unzipped Values :-')
print(list(pos), type(list(pos)))
print(names)
print(roll)


   