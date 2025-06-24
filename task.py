# a = [1, 2, 3]
# b = [3, 4, 5]
# c = set(a)
# v = set(b)
# n = c.intersection(v)
# n = list(sorted(n))
# print(n)


a = set(range(52))

q = set(range(23))

w = set(range(35))

y = set(range(16))

t = set(w.update(q))
e = (t.difference(y))
l = (a-e)


print(l)
