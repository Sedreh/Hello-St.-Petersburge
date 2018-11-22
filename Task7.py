import re
from functools import reduce
from itertools import chain
import functools
import numpy as np


# 1
def valuesunion(*dicts):
    return set().union(chain.from_iterable([x.values() for x in dicts]))


# 2
def popcount(n):
    count = 0
    while n > 0:
        count += 1
        n &= n - 1
    return count


# 3
def powers(n, m):
    return dict([(i, i ** (i % m)) for i in range(1, n + 1)])


# 4
def subpalindrome(s):
    rev = s[::-1]
    l = len(s)
    while l > 0:
        for i in range(0, len(s) - l + 1):
            half = int(l / 2)
            left = s[i: i + half]
            right = rev[len(s) - (i + l): len(s) - (i + l - half)]
            if left == right:
                return s[i:i + l]
        l -= 1
    return None


# 5
def isIPv4(s):
    return re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", s) is not None


# 6
def pascals():
    res = (1,)

    for i in itertools.count(1):
        act = []
        act.append(1)
        for k in range(len(res) - 1):
            act.append(res[k] + res[k + 1])
        act.append(1)
        yield tuple(res)
        res = act


# 7
def spiral(n):
    a = np.arange(n * n)
    b = a.reshape((n, n))
    m = None
    for i in range(n, 0, -2):
        m = np.r_[m, b[0, :], b[1:, -1], b[-1, :-1][::-1], b[1:-1, 0][::-1]]
        b = b[1:-1, 1:-1]
    a[list(m[1:])] = list(a)
    return a.reshape((n, n)) + 1


# 8
def fibonacci(n):
    return functools.reduce(lambda x, n: [x[1], x[0] + x[1]], range(n), [0, 1])[0]


# 9
def brackets2(n, m):
    def compute_parens(left, right, s):
        if right == n:
            yield s
            return
        if left < n:
            yield from compute_parens(left + 1, right, s + "(")
        if right < left:
            yield from compute_parens(left, right + 1, s + ")")

    yield from compute_parens(0, 0, "")

    def compute_brac(left, right, k):
        if right == m:
            yield k
            return
        if left < m:
            yield from compute_brac(left + 1, right, k + "[")
        if right < left:
            yield from compute_brac(left, right + 1, k + "]")

    yield from compute_brac(0, 0, "")


[x for x in brackets2(2, 0) if x != ""]
