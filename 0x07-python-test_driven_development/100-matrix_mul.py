#!/usr/bin/python3
''' function that multiplies 2 matrices '''


def matrix_mul(m_a, m_b):
    ''' function that multiplies 2 matrices '''
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for lst in m_a:
        if not isinstance(lst, list):
            raise TypeError("m_a must be a list of lists")
    for lst in m_b:
        if not isinstance(lst, list):
            raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")
    for lst in m_a:
        for i in lst:
            if not (isinstance(i, int) or isinstance(i, float)):
                raise TypeError("m_a should contain only integers or floats")
    for lst in m_b:
        for i in lst:
            if not (isinstance(i, int) or isinstance(i, float)):
                raise TypeError("m_b should contain only integers or floats")
    asize = len(m_a[0])
    for lst in m_a:
        if len(lst) != asize:
            raise TypeError("each row of m_a must be of the same size")
    bsize = len(m_b[0])
    for lst in m_b:
        if len(lst) != bsize:
            raise TypeError("each row of m_b must be of the same size")
    if asize != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    mul = [[] for i in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            m = 0
            for k in range(len(m_b)):
                m += m_a[i][k] * m_b[k][j]
            mul[i].append(m)

    return mul


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
