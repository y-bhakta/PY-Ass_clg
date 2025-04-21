import pandas as pa
data=pa.read_csv('data.csv')
print("Data Dictionary: ")
print("---------------------------------------")
print(data)
print("---------------------------------------")
print("Total Numbers of student: ", len(data))