'''
STLPY is a module which will help you in any competition and your dsa journey
Please share this with your friend too.
Creaters - Shashwat & Rudransh
'''

print("Please share this module with your friends if you like it and \n all the functions are available in the documentation : enjoy your CODE!!")

def SieveOfEratosthenes(num):
    prime = [True for i in range(num+1)]
    p = 2
    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
    for p in range(2, num+1):
        if prime[p]:
            return prime


def reverse_array(arr):
    return arr[::-1]


def addtoall_array(arr, num):
    for i in arr:
        arr[i] += num
    return arr


def primeatn(n):
    try:
        n = int(n)
        prime_numbers = [2, 3]
        i = 3
        if (0 < n < 3):
            return prime_numbers[n-1]
        elif (n > 2):
            while (True):
                i += 1
                status = True
                for j in range(2, int(i/2)+1):
                    if (i % j == 0):
                        status = False
                        break
                if (status == True):
                    prime_numbers.append(i)
                if (len(prime_numbers) == n):
                    break
            return prime_numbers[n-1]
    except:
        print("Something went wrong try again with right inputs")


def frequency_array(arr,k):
    ct = 0
    for i in arr:
        if(k==arr[i]):
            ct += 1
    return ct

def factorial(num):
    fact=1
    yo = 1
    if(num<1):
        yo = 0
        fact = None
    if(num==1 or num==0):
        y = 0
        fact = 1
    if(yo==1):
        for i in range(1,num+1):
            fact = fact * i
    return fact

