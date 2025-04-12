capitals = {"India" : "New Delhi", 
            "USA" : "Washington",
            "Japan" : "Tokyo",
            "France" : "Paris",
            "Germany" : "Berlin"}
print(capitals)
print(capitals.get('USA'))
print(capitals.pop('Germany'))
print(capitals.popitem())
c1=capitals.copy()
print(capitals)
print(c1)
capitals.clear()
print(capitals)