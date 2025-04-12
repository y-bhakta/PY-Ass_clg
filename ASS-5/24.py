s = {
    "John": 85,
    "Jane": 90,
    "Doe": 78
}
print(s)
print("Highest Marks is of: ")
print(max(s,key=s.get))