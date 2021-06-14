'''
As this is only going to i*i of n and not for the whole n 
it can also be considered as  i squared <=n or i <= root(n)
therefore O becomes O(root(n))
'''

import sys

def isPrime(n):
    for i in range(2,n):
        if i*i <= n and n%i == 0:
                # print(n, 'is not prime')
            return
    print(n, 'is prime')

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print('Please add an argument to check if its prime')
        exit()

    val = str(sys.argv[1])
    if not val.isnumeric():
        print('Only accepting numbers')
        exit()

    for i in range(1,int(val)):
        isPrime(int(i))