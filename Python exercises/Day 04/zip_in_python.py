name =['disas','david','dilini','dulan']
age=[9,10,39,41]

combination = list(zip(name,age))
for name,age in combination:
    print(f'{name} is {age} years old')
