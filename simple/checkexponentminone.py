from isprime import isPrime
import sys

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print('Please add an argument to check if exponent is prime')
        exit()

    val = str(sys.argv[1])
    if not val.isnumeric():
        print('Only accepting numbers')
        exit()

    for i in range(int(val)):
        print('trying for i',i , 'as ', pow(2, i) - 1)
        isPrime(pow(2, i) - 1)
