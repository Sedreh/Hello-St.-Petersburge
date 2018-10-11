__author__ = 'DELLIRAN'

#Q1
def listToString(a):
    assert type(a) == list
    return str(a)

print(listToString([1,2,3]))

#Q2
import numpy as np
import string

def addBorder(a):
    border = ['+' + string.join(np.repeat('-',len(a[0])),'') + '+']
    a = ['|' + x  + '|' for x in a]
    return (border + a + border)
pip install numpy


#Q3
def shorting(e):
    assert type(e) == list
    for X in range(len(e)):
        if len(e[X]) > 10:
            e[X] = e[X][0] + str(len(e[X]) - 2) + e[X][len(e[X]) - 1]
    return e

print(shorting(['word', 'localization', 'internationalization',
          'pneumonoultramicroscopicsilicovolcanoconiosis']))

#Q5
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

#Q6
def makeShell(n):
	shell=[]
	for x in range(n):
		shell+= [[0]*(x+1)]
	for x in range(n-1,0,-1):
		shell+= [[0]*x]
	return shell
