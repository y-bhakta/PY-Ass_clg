d1= {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}
d2 = {}
for key, value in d1.items():
    if value not in d2:
        d2[value] = [key]
    else:
        d2[value].append(key)
print(d2)