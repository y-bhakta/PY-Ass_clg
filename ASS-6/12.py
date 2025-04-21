import pandas as pd
data = {
'name':['Anash', 'Daksh', 'Deep'],
'age' :[19, 18, 20]
}
df = pd.DataFrame(data)
result = df.iloc[2,1]
print(result)