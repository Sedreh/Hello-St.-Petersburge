__author__ = 'DELLIRAN'


# Q1

def permutations(n):
    def perm_n(n, pref=[]):
        if len(pref) == n:
            yield tuple(pref)
        else:
            s = set(pref)
            for i in range(1, n + 1):
                if i not in s:
                    yield from perm_n(n, pref + [i])

    return list(perm_n(n))


# Q2

def correctbracketsequences(n):
    def correctbracketsequences1(n, buf='', balance=0):
        if len(buf) == 2 * n and balance == 0:
            yield buf
        else:
            for i in ('(', ')'):
                new_buf = buf + i
                new_balance = balance + (1 if i == '(' else -1)
                if len(new_buf) <= 2 * n and new_balance >= 0:
                    yield from correctbracketsequences1(n, new_buf, new_balance)

    return list(correctbracketsequences1(n))


# Q3

def combinationswithrepeats(n, k):
    def comb_n(n, k, pref=[]):
        if len(pref) == k:
            yield tuple(pref)
        else:
            m = max(pref) if len(pref) > 0 else 1
            for i in range(m, n + 1):
                yield from comb_n(n, k, pref + [i])

    return list(comb_n(n, k))


# Q4

def unorderedpartitions(n):
    out = []
    tmp = []
    sub_nums = range(1, n + 1)
    for num in sub_nums:
        if num <= n:
            tmp.append([num])
        for elm in tmp:
            sum_elm = sum(elm)
            if sum_elm == n:
                out.append(elm)
            else:
                for num in sub_nums:
                    if sum_elm + num <= n:
                        L = [i for i in elm]
                        L.append(num)
                        tmp.append(L)
    return out


if __name__ == "__main__":
    assert permutations(1) == [(1,)]
    assert permutations(2) == [(1, 2), (2, 1)]
    assert permutations(3) == [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
    print("permutations - OK")

    assert correctbracketsequences(1) == ['()']
    assert correctbracketsequences(2) == ['(())', '()()']
    assert correctbracketsequences(3) == ['((()))', '(()())', '(())()', '()(())', '()()()']
    print("correctbracketsequences - OK")

    assert combinationswithrepeats(1, 1) == [(1,)]
    assert combinationswithrepeats(2, 2) == [(1, 1), (1, 2), (2, 2)]
    assert combinationswithrepeats(3, 2) == [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
    print("combinationswithrepeats - OK")


