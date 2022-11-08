'''
STLPY is a module which will help you in any competition and your dsa journey
Please share this with your friend too.
Creaters - Shashwat & Rudransh
'''

print("Hello! from team stlpy (Shashwat and Rudransh)")


# def SieveOfEratosthenes(num):
#     prime = [True for i in range(num+1)]
#     p = 2
#     while (p * p <= num):
#         if (prime[p] == True):
#             for i in range(p * p, num+1, p):
#                 prime[i] = False
#         p += 1
#     for p in range(2, num+1):
#         if prime[p]:
#             return prime


class array:

    @staticmethod
    def reverse_array(arr):
        return arr[::-1]

    @staticmethod
    def addtoall(arr, num):
        for i in range(len(arr)):
            arr[i] += num
        return arr

    @staticmethod
    def frequency(arr, k):
        ct = 0
        for i in arr:
            if (k == arr[i]):
                ct += 1
        return ct


class number:
    @staticmethod
    def power(x, y):

        if y == 0:
            return 1
        if y % 2 == 0:
            return number.power(x, y // 2) * number.power(x, y // 2)

        return x * number.power(x, y // 2) * number.power(x, y // 2)

    @staticmethod
    def order(x):
        n = 0
        while (x != 0):
            n = n + 1
            x = x // 10
        return n

    @staticmethod
    def nthFibonacci(num):
        if num <= 2:
            return num - 1
        else:
            return number.nthFibonacci(num - 1) + number.nthFibonacci(num - 2)

    @staticmethod
    def factorial(num):
        fact = 1
        if (num < 1):
            fact = None
        elif (num == 1 or num == 0):
            fact = 1
        else:
            for i in range(1, num+1):
                fact = fact * i
        return fact

    @staticmethod
    def gcd(x, y):
        while (y):
            x, y = y, x % y
        return x

    @staticmethod
    def lcm(x, y):
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

    @staticmethod
    def nCr(n, r):
        return (number.factorial(n))/((number.factorial(r))*number.factorial(n-r))

    @staticmethod
    def nPr(n, r):
        return (number.factorial(n))/(number.factorial(n-r))

    @staticmethod
    def isArmstrong(x):
        n = number.order(x)
        temp = x
        sum1 = 0
        while (temp != 0):
            r = temp % 10
            sum1 = sum1 + number.power(r, n)
            temp = temp // 10
        return (sum1 == x)


class dsa:
    @staticmethod
    def binary_search(arr, low, high, key):
        if high >= low:
            mid = (high + low) // 2
            if arr[mid] == key:
                return mid
            elif arr[mid] > key:
                return dsa.binary_search(arr, low, mid - 1, key)
            else:
                return dsa.binary_search(arr, mid + 1, high, key)
        else:
            return -1
