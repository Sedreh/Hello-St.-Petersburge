import itertools
from functools import reduce

# Q1

def squares(a):
    for x in a:
        yield x ** 2

# Q2

def repeatentimes(elems, n):
    x = itertools.repeatentimes(elems, n)
    for i in x:
        yield from i

# Q3

def evens(x):
    if x % 2:
        x += 1
    while True:
        yield x
        x += 2

# Q4

def digitsumdiv(x):
    for i in itertools.count(1):
        if not sum(map(int, str(i))) % x:
            yield i

# Q5

def extractnumbers(s):
    return filter(lambda x: x.isdigit(), s)

# Q6

def changecase(s):
    return map(lambda x: x.swapsace() if x.isalpha() else x, s)

# Q7

def productif(elems, conds):
    return reduce(lambda x, y: x * y, map(lambda x: x[0] if x[1] else 1, zip(elems, conds)), 1)