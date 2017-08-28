def min(vec):
    res = vec[0]
    for el in vec:
        if (res > el): res = el
    return res

print min ((7,6,4,5,3,1,2))
