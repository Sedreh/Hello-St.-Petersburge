import numpy as np


# Q2

def getdiagonal(a):
    return np.diagonal(a)


# Q3

def cutarray(a, minvalue, maxvalue):
    return np.clip(a, minvalue, maxvalue)


# Q4

def getmoments(a):
    return np.mean(a), np.var(a)


# Q5

def getdotproduct(a, b):
    return np.dot(a, b)


# Q6

def checkequal(a, b):
    return a == b


# Q8

def matrixproduct(a, b):
    return np.matmul(a, b)


# Q9

def matrixdet(a):
    return np.linalg.det(a)


# Q10

def getones(n, k):
    return np.eye(n, k=k)


# Q1

def getdimension(a):
    return len(a.shape)


# Q7

def comparewithnumber(a, bound):
    return a < bound


if __name__ == "__main__":

    assert np.array_equal(np.array(getdiagonal(np.array([[1, 2], [3, 4]]))), np.array([1, 4]))
    print("getdiagonal - OK")

    assert np.array_equal(cutarray(np.array([1, 2, 3, 4]), 2, 3),
                          np.array([2, 2, 3, 3]))
    print("cutarray - OK")

    assert getmoments(np.array([2, 1, 9])) == (4.0, 12.666666666666666)
    print("getmoments - OK")

    assert getdotproduct(np.array([1, 2, 3]), np.array([4, 5, 6])) == 32
    print("getdotproduct - OK")

    assert np.array_equal(checkequal(np.array([1, 2, 3]), np.array([1, 5, 3])),
                          np.array([True, False, True]))
    print("checkequal - OK")

    assert np.array_equal(matrixproduct(np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]])),
                          np.array([[19, 22], [43, 50]]))
    assert np.array_equal(matrixproduct(np.array([[1, 2]]), np.array([[3], [4]])),
                          np.array([[11]]))
    print("matrixproduct - OK")

    assert int(matrixdet(np.array([[5, 6], [7, 8]]))) == -2
    assert int(round(matrixdet(np.array([[123]])))) == 123
    print("matrixdet - OK")

    assert np.array_equal(getones(3, 1), np.array([[0., 1., 0.],
                                                   [0., 0., 1.],
                                                   [0., 0., 0.]]))
    assert np.array_equal(getones(3, 9), np.array([[0., 0., 0.],
                                                   [0., 0., 0.],
                                                   [0., 0., 0.]]))
    print("getones - OK")

    assert getdimension(np.array([1, 2, 3])) == 1
    assert getdimension(np.array([[1], [2], [3]])) == 2
    assert getdimension(np.array([[[[1]]]])) == 4
    print("getdimension - OK")

    assert np.array_equal(comparewithnumber(np.array([[1, 2], [3, 4]]), 4),
                          np.array([[True, True], [True, False]]))
    print("comparewithnumber - OK")
