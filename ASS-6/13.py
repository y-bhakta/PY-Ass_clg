import pandas as pd
data = {
'Name':['rushabh','ved','daksh','anash'],
'Dept':['Hr','finances','IT','Marketing'],
'salary':[60000, 50000, 55000, 45000]
}
df = pd.DataFrame(data)
highest_salary = df.loc[df ['salary'] > 50000]
print(highest_salary)
