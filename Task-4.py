__author__ = 'DELLIRAN'


# Q1

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

# Q2

def fibonacci(n):
    if n==1:
        return 1
    if n==2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


# Q4

def sum_digits(number):
    if number < 10:
        return n
    else:
        # Mod (%) by 10 gives the rightmost digit (227 % 10 == 7),
        # while doing integer division by 10 removes the rightmost

        return (number % 10) + sumdigits(number // 10)

#Q 5

def reversestring(text):
    if text==" ":
        return text
    else:
        return text[-1]+ backward(text[: -1])


#Q 6

def ack_recursive(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return ack_recursive(m - 1, 1)
    return ack_recursive(m - 1, ack_recursive(m, n - 1))


#Q 9

def istwopower(n):
    return n > 0 and (n & (n - 1)) == 0

# Q10

def concatnumbers(a, b):
    return a * (10**len(str(b))) + b


# Q13

def gcd2(m, n):
    if m % n != 0:
        return gcd2(n, m % n)
    else:
        return n
# Q14

def merge_sort(a):
    merge_sort2(a, 0, len(a) - 1)
def merge_sort2(a, first, last):
    if first < last:
        middle = (first + last)// 2
        merge_sort2(a, first, middle)
        merge_sort2(a, middle + 1, last)
        merge(a, first, middle, last)
def merge(a, first, middle, last):
    left1 = a[first:middle]
    right1 = a[middle:last + 1]
    left1.append(99999999999)
    right1.append(99999999999)
i = j = 0
for k in range(first, last + 1):
    if left1(i) <= right1(j):
        a[k] = left1(i)
        i += 1
    else:
        a[k] = right1[j]
        j += 1


if __name__ == "__main__":
    assert factorial(4) == 24
    assert factorial(0) == 1
    assert factorial(2) == 2
    print('factorial - OK')

    assert fibonacci(1) == 1
    assert fibonacci(4) == 3
    assert fibonacci(10) == 55
    print('fibonacci - OK')

    assert sum_digits(0) == 0
    assert sum_digits(123) == 6
    assert sum_digits(192837465) == 45
    print('sum_digits - OK')

    assert reversestring('') == ''
    assert reversestring('1') == '1'
    assert reversestring('asdf') == 'fdsa'
    assert reversestring('abacaba') == 'abacaba'
    print('reversestring - OK')

    assert ack_recursive(0, 10) == 11
    assert ack_recursive(1, 1) == 3
    assert ack_recursive(2, 2) == 7
    assert ack_recursive(2, 5) == 13
    assert ack_recursive(3, 3) == 61
    print('ack_recursive - OK')

    assert istwopower(-5) is False
    assert istwopower(0) is False
    assert istwopower(1) is True
    assert istwopower(2) is True
    assert istwopower(4) is True
    assert istwopower(67) is False
    assert istwopower(1024) is True
    print('istwopower - OK')

    assert concatnumbers(1, 2) == 12
    assert concatnumbers(55, 88) == 5588
    assert concatnumbers(123, 789) == 123789
    assert concatnumbers(1000, 2) == 10002
    print('concatnumbers - OK')

    assert gcd2(1, 5) == 1
    assert gcd2(4, 6) == 2
    assert gcd2(18, 12) == 6
    assert gcd2(283918822, 595730520) == 22
    print('gcd2 - OK')

    assert merge_sort([]) == []
    assert merge_sort([100]) == [100]
    assert merge_sort([1, 3, 2]) == [1, 2, 3]
    assert merge_sort([1, 3, 5, 4, 2]) == [1, 2, 3, 4, 5]
    print('merge_sort - OK')