print('hello world')
# age = int(input('when were you born'))
# year = int(input('what is the year now'))
# current_Age = year-age
# print('Your age as of present is',current_Age)

# weight = int(input('What is your weight in kgs?'))
# lbs_weight = weight*2.20462
# print('Your weight in lbs is',lbs_weight)

print(10/3)
#(= 3.3333)
print(10//3)
#(= 3)
print(10%3)
#(= 1)
print(10 ** 3)
#(= 1000 or 10 to power of 3)


num = int(input('enter a number : '))
i=0
while i < 11:
    print(i*num)
    i = i + 1


year = int(input('enter the year'))
if year%4 == 0:
    print('the year is a leap year')
else:
    print('the year is not a leap year')



number = int(input('what is the number : '))
if number%2 == 1:
    print('the number is odd')
else:
    print('the number is even')



primnum = int(input('enter the number : '))
if primnum == 1:
    print(primnum, "is not a prime number")
elif primnum > 1:
    # check for factors
    for i in range(2, num):
        if (primnum % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

    # check if flag is True
    if flag == False:
        print(primnum, "is not a prime number")
    else:
        print(primnum, "is a prime number")








