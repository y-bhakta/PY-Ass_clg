import pandas as pd
data = pd.read_csv('data.csv')
print(data[data['Marks'] > 70]["Name"])