import itertools


# Q1


def permutations(n):
    return list(itertools.permutations(range(1, n + 1)))


print(list(permutations(3)))


# Q2


def correctbracketsequences(output, openb, close, pairs):
    if openb == pairs and close == pairs:
        print(output)
    else:
        if openb < pairs:
            correctbracketsequences(output + '(', openb + 1, close, pairs)
        if close < openb:
            correctbracketsequences(output + ')', openb, close + 1, pairs)


print(correctbracketsequences('', 0, 0, 2))


# Q3

def combinationwithrepeat(n, r):
    return list(itertools.combinations_with_replacement(range(1, n + 1), r))


print(combinationwithrepeat(1, 1))


# Q4


def partitions_tuple(n):
    if n == 0:
        yield []
        return
    for p in partitions_tuple(n - 1):
        yield [1] + p
        if p and (len(p) < 2 or p[1] > p[0]):
            yield [p[0] + 1] + p[1:]


print(list(partitions_tuple(5)))

if __name__ == "__main__":
    assert permutations(1) == [(1,)]
    assert permutations(2) == [(1, 2), (2, 1)]
    assert permutations(3) == [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

    print("permutations - done!")

    assert correctbracketsequences('', 0, 0, 1) == ['()']
    assert correctbracketsequences('', 0, 0, 2) == ['(())', '()()']
    assert correctbracketsequences('', 0, 0, 3) == ['((()))', '(()())', '(())()', '()(())', '()()()']

    print("correctbracketsequences - done!")

    assert combinationwithrepeat(1, 1) == [(1,)]
    assert combinationwithrepeat(2, 2) == [(1, 1), (1, 2), (2, 2)]
    assert combinationwithrepeat(3, 2) == [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]

print("combinationwithrepeat - done!")

assert partitions_tuple(1) == [(1,)]
assert partitions_tuple(3) == [(1, 1, 1), (1, 2), (3,)]
assert partitions_tuple(5) == [(1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 1, 3), (1, 2, 2), (1, 4), (2, 3), (5,)]

print("partitions_tuple - done!")
