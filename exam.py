import re
from functools import reduce


def subpalindrome1(s):
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


def valuesunion(*dicts):
    return set().union(chain.from_iterable([x.values() for x in dicts]))


def powers(n, m):
    return dict([(i, i ** (i % m)) for i in range(1, n + 1)])


def popcount(n):
    count = 0
    while n > 0:
        count += 1
        n &= n - 1
    return count


def isipv4(ip):
    return re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip) != None


fib=lambda n:reduce(lambda x,y:(x[0]+x[1],x[0]),[(1,1)]*(n-2))[0]


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