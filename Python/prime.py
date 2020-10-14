#roblem: Have the function PrimeTime(num) 
# take the num parameter being passed and return 
# the string true if the parameter is a prime number, \
# otherwise return the string false.
#  The range will be between 1 and 2^16.

def PrimeTime(num):

    prime1 = (num-1)%6
    prime2 = (num+1)%6

    if prime1 * prime2 == 0:
        return 'True'
    else:
        return 'False'

print(PrimeTime(12))