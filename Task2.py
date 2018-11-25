__author__ = 'DELLIRAN'


import numpy as np
import string


# Q1
def listToString(a):
    assert type(a) == list, "listToString argument is not a list"
    return str(a)


# Q2
def addBorder(a):
    border = ['+' + ''.join(np.repeat('-', len(a[0]))) + '+']
    a = ['|' + x + '|' for x in a]
    return border + a + border


# Q3
def shorting(e):
    assert type(e) == list
    for X in range(len(e)):
        if len(e[X]) > 10:
            e[X] = e[X][0] + str(len(e[X]) - 2) + e[X][len(e[X]) - 1]
    return e


# Q4
def competition(e, k):
        advanced = 0
        for i in range(len(e)):
            if e[i] >= e[k] and e[i] > 0:
                advanced += 1
        return advanced

# Q5
def goodPairs(a, b):
    y = []
    y_set = set()
    for i in a:
        for j in b:
            if (i * j) % (i + j) == 0:
                s = (i ** 2 + j ** 2)
                if s not in y_set:
                    y.append(s)
                    y_set.add(s)
    y.sort()
    return y

# Q6
def makeShell(n):
    shell = []
    for x in range(n):
        shell += [[0] * (x + 1)]
    for x in range(n - 1, 0, -1):
        shell += [[0] * x]
    return shell


if __name__ == "__main__":

    assert listToString([]) == "[]", "listToString error"
    assert listToString([1, 2, 3]) == "[1, 2, 3]", "listToString error"
    assert listToString([-5]) == "[-5]", "listToString error"
    print("listToString - OK")


    assert addBorder(['abc',
                      'def']) == ['+---+',
                                  '|abc|',
                                  '|def|',
                                  '+---+'], \
        "addBorder error"
    print("addBorder - OK")


    assert shorting(['word', 'localization', 'internationalization',
                    'pneumonoultramicroscopicsilicovolcanoconiosis']) == \
        ['word', 'l10n', 'i18n', 'p43s'], "shorting error"
    print("shorting - OK")


    assert competition([5, 4, 3, 2, 1], 2) == 3, \
        "competition error"
    assert competition([1, 0, 0, 0], 3) == 1, \
        "competition error"
    assert competition([10, 9, 8, 7, 7, 7, 5, 5], 4) == 6, \
        "competition error"
    print("competition - OK")


    assert goodPairs([4, 5, 6, 7, 8], [8, 9, 10, 11, 12]) == [128, 160, 180], \
        "goodPairs error"
    assert goodPairs([2], [2]) == [8], \
        "goodPairs error"
    assert goodPairs([7, 8, 9], [5, 3, 2]) == [], \
        "goodPairs error"
    print("goodPairs - OK")


    assert makeShell(1) == [[0]], "makeShell error"
    assert makeShell(2) == [[0], [0, 0], [0]], "makeShell error"
    assert makeShell(3) == [[0], [0, 0], [0, 0, 0], [0, 0], [0]], \
        "makeShell error"
    print("makeShell - OK")