import pandas as pa
data={
    'Name':['Tom','Jerry','Mickey','Donald','John'],
    'department':['CS','IT','HR','HR','Finance'],
    'salary':[20000,21000,22000,23000,25000]
}
df=pa.DataFrame(data)
print("Data Dictionary: ")
print("---------------------------------------")
print(df.head(3))
print("---------------------------------------")
print(df['Name'],df['salary'])
print("---------------------------------------")
print(df[df['department']=='HR']['salary'])
print("---------------------------------------")