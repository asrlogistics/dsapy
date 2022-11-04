'''
STLPY is a module which will help you in any competition and your dsa journey
Please share this with your friend too.
Creaters - Shashwat & Rudransh
'''

print("##### Please share this module with your friends if you like it and \n all the functions are available in the documentation \n : enjoy your CODE!! \n \n \n \n")


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


class array:
    def __init__(self, arr):
        self.arr = arr

    def reverse_array(self, arr):
        return arr[::-1]

    def addtoall(self, arr, num):
        for i in range(len(arr)):
            arr[i] += num
        return arr

    def frequency(self, arr, k):
        ct = 0
        for i in arr:
            if (k == arr[i]):
                ct += 1
        return ct


class number:
    def __init__(self, num):
        self.num = num

    def factorial(self, num):
        fact = 1
        yo = 1
        if (num < 1):
            yo = 0
            fact = None
        if (num == 1 or num == 0):
            y = 0
            fact = 1
        if (yo == 1):
            for i in range(1, num+1):
                fact = fact * i
        return fact

    def gcd(self, x, y):
        while (y):
            x, y = y, x % y
        return x

    def lcm(self,x, y):
        if x > y:
            greater = x
        else:
            greater = y
        while (True):
            if ((greater % x == 0) and (greater % y == 0)):
                lcm = greater
                break
            greater += 1
        return lcm
