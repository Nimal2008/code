weight = input('Please enter your weight: ')
unit = input('pounds(l) or (k) for kilograms')
if unit.upper() == ('L'):
    weight_kilograms = (int(weight) * 0.45)
elif unit.upper() == ('K'):
    weight_pounds = (int(weight//0.45))






i = ('[')
g = (']')
h = ('Nimal'+ i +'Senthilkumar' + g + 'is a coder')
print(h)

Name = ('Nimal')
print('Ni' in Name)

print(10/3)
print(10*3)
print(10+3)
print(10%3)
print(10//3)
print(10-3)
print(10**3)

x= 10
x+= 3
print (x)
x-= 3
print (x)
x+= -1.45
print(round(x))
print(abs(x))

username = input('please enter an username: ')
length = len(username)
print(length)
if length >= 3 and length<= 50:
    print('username is good to go')
else:
    print('Username must be above 3 characters long and below 50 characters long. ')
