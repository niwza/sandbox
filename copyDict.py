def copyDict(dic):
    res = {}
    for key in dic.keys():
        res[key] = dic[key]
    return res


D = {'a':2, 'b':3}
X = copyDict(D)
print(X is D)
