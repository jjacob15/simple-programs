from sys import prefix


def permutation(str):
    compute(str,"")

count = 0
def compute(str,prefix):
    print('compute', str, prefix)
    if len(str) == 0:
        print(prefix)
    else:
        for i in range(len(str)):
            rem = str[0:i] + str[i+1:]
            print('rem', rem)
            compute(rem, prefix + str[i])

permutation("abc")