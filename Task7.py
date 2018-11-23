import re
from functools import reduce
from itertools import chain
import functools
import numpy as np
import itertools

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
def subpalindrome(string):
    def check(word):
        if len(word) == 1:
            return True
        return all(word[i] == word[-1 * (i + 1)] for i in range(len(word) // 2))

    subpal = ''
    max = 0
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            if check(string[i:j]):
                if j - i > max:
                    subpal = string[i:j]
                    max = j - i
                elif j - i == max:
                    if string[i:j] < subpal:
                        subpal = string[i:j]

    return subpal


# 5
def isIPv4(s):
    return re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", s) is not None


# 6
def pascals():
    prev = (1,)

    for i in itertools.count(1):
        act = []
        act.append(1)
        for k in range(len(prev) - 1):
            act.append(prev[k] + prev[k + 1])
        act.append(1)
        yield tuple(prev)
        prev = act


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

if __name__ == "__main__":
    assert valuesunion({1: 2, 4: 8}) == {2, 8}
    assert valuesunion({1: 2}, {4: 8}) == {2, 8}
    assert valuesunion({1: 2, 4: 8}, {'a': 'b'}, {}, {}) == {2, 8, 'b'}
    print("valuesunion - OK")

    assert popcount(0) == 0
    assert popcount(1) == 1
    assert popcount(10) == 2
    assert popcount(1023) == 10

    assert subpalindrome('abc') == 'a'
    assert subpalindrome('aaaa') == 'aaaa'
    assert subpalindrome('abaxfgf') == 'aba'
    assert subpalindrome('abacabad') == 'abacaba'
    print("subpalindrome - OK")

    assert spiral(1) == [[1]]
    assert spiral(2) == [[1, 2],
                         [4, 3]]
    assert spiral(4) == [[1, 2, 3, 4],
                         [12, 13, 14, 5],
                         [11, 16, 15, 6],
                         [10, 9, 8, 7]]
    print("spiral - OK")

    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    print("fibonacci - OK")

    assert list(brackets2(1, 0)) == ['()']
    assert list(brackets2(0, 1)) == ['[]']
    assert list(brackets2(1, 1)) == ['()[]', '([])', '[()]', '[]()']
    assert list(brackets2(3, 0)) == ['((()))', '(()())', '(())()', '()(())',
                                     '()()()']
    assert list(brackets2(2, 1)) == ['(())[]', '(()[])', '(([]))', '()()[]',
                                     '()([])', '()[()]', '()[]()', '([()])',
                                     '([]())', '([])()', '[(())]', '[()()]',
                                     '[()]()', '[](())', '[]()()']
    print("brackets - OK")
    print(subpalindrome("qfryinzykktqbvgdzaggxyjkw"))
