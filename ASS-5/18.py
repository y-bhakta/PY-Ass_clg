s={'a','e','i','o','u','A','O','E','I','U'}
s1=str(input("Enetr a string: "))
for char in s1:
    if char in s:
        s1=s1.replace(char,' ')
print(s1)        