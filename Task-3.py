import itertools

__author__ = 'DELLIRAN'


# Q1


def squares(a):
    for x in a:
        yield x ** 2


# Q2


def repeatentimes(e, n):
    x = itertools.repeat(e, n)
    for i in x:
        yield from i


# Q3

def evens(i):
    if i % 2:
        i += 1
    while True:
        yield i
        i += 2

# Q4


def digitsumdiv(x):
    for i in itertools.count(1):
        if not sum(map(int, str(i))) % x:
            yield i

# Q5


def extractnumbers(my_list):
    return filter(lambda x: x.isdigit(), my_list)

# Q6

def changecase(my_list):
    return map(lambda x: x.swapsace() if x.isletter() else x , my_list)


# Q7

 def productif(elems, conds):
    ????????????