def reverse(text):
    lst = list(text)
    st = ""
    i = len(lst)
    while i > 0:
        st += lst[i-1]
        i -= 1
    return st

print(reverse("Python!"))
