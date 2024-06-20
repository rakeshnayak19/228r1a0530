 def remove_dup(li):
    u = []
    d = []
    for i in li:
        if i not in u:
            u.append(i)
        else:
            d.append(i)
    return u


li = [1, 2, 3, 4, 5, 5, 3, 2, 1]
print(li)
print(remove_dup(li))