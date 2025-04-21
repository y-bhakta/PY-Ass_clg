import pandas as pd
data = {
'Name':['yash','deep','krishna','daksh'],
'Dept':['Hr','finances','IT','Marketing'],
'salary':[50000, 60000, 45000, 75000]
}
df = pd.DataFrame(data)
row_index_0 = df.loc[0, :]
print("\n all column for the row with index 0:\n", row_index_0)
slice_column_index = df.loc[[1, 3] , ['Name', 'Dept']]
print("\n slice row from 1 to 3 and selected col (name and dept):\n",
slice_column_index)
