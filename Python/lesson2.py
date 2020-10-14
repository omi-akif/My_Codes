a=int(input('Enter a number'))
if a%4==0 :
    print('It is a leap year')
elif a%100==0 :
    print('It is a leap year')
elif a%400==0 :
    print('It is a leap year')
else :
    print('It is not a leap year')