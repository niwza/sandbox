def adder(**arg):
    lst = list(arg.keys())
    res = arg[lst[0]]
    for x in lst[1:]:
        res += arg[x]
    return res

print(adder(a=4,foo=3,b=5))
print(adder(A='spam',B='foo'))

