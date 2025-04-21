import pandas as pa
data={
    'Name':['Tom','Jerry','Mickey','Donald'],
    'Age':[20,21,22,23],
    'City':['New York','Los Angeles','Chicago','Houston'],
}
print("Data Dictionary: ")
print(pa.DataFrame(data))
print("---------------------------------------")
print("First Row: ")
print(pa.DataFrame(data).head(1))
print("---------------------------------------")
print("Last Row: ")
print(pa.DataFrame(data).tail(1))

