__author__ = 'DELLIRAN'

# Q1

def unique(e):
    return sorted(list(set(e)))


# Q2
def transpose_dict(d):
    return dict([(v, k) for k, v in d.items()])


# Q3
def mex(e):
    return next(i for i in range(1, len(e) + 2) if i not in set(e))


# Q5
def frequencyDict(s):
    return {ch: s.count(ch) for ch in set(s)}


if __name__ == "__main__":

    assert unique([1, 2, 1, 3]) == [1, 2, 3], "unique func. error"
    assert unique({5, 1, 3}) == [1, 3, 5], "unique func. error"
    assert unique('adsfasdf') == ['a', 'd', 'f', 's'], "unique func. error"
    print("unique func. - OK")

    assert transpose_dict({}) == {}, "transposeDict func. error"
    assert transpose_dict({1: 'a', 2: 'b'}) == {'a': 1, 'b': 2}, \
        "transposeDict func. error"
    assert transpose_dict({1: 1}) == {1: 1}, "transposeDict func. error"
    print("transposeDict func. - OK")

    assert mex([1, 2, 3]) == 4, "mex func. error"
    assert mex(['asdf', 123]) == 1, "mex func. error"
    assert mex([0, 0, 1, 0]) == 2, "mex func. error"
    print('mex func. - OK')

    assert frequencyDict('') == {}, "frequencyDict func. error"
    assert frequencyDict('abacaba') == {'a': 4, 'b': 2, 'c': 1}, \
        "frequencyDict func. error"
    print("frequencyDict func. - OK")
