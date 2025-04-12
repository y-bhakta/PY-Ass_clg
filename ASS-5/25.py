words = list(input("Enter words separated by spaces: ").split())
dict= {}
for i in words:
    dict[i]=len(i)

print(dict)