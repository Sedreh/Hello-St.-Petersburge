__author__ = 'DELLIRAN'
#def unique(e)
def unique(e):
    # unique_e1 = []
    # for x in e:
    #     if x not in unique_e1:
    #         unique_e1.append(x)
    # # for x in unique_e1:
    # #     print (x)
    # unique_e1.sort()
    # return unique_e1
    return sorted(list(set(e)))


#def transposeDict(d)
def transpose_dict(d):
    return dict([(v, k) for k, v in d.items()])

d = {'child1': 'parent1',
     'child2': 'parent2',
     }


#def mex(e):
def mex(e):
    return next(i for i in range(1, len(e)+2) if i not in set(e))


#frequencyDict(s):
from collections import Counter

def frequencyDict(s):
    return dict(Counter(s))
print(frequencyDict("abbdhbhsbdbcd"))
