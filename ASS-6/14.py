import pandas as pd
data = {
'Name':['yash','ved','daksh','anash'],
'Dept':['Hr','finances','IT','Marketing'],
'salary':[50000, 60000, 45000, 75000]
}
df = pd.DataFrame(data)
third_row = df.iloc[2]
print("\nthird row\n",third_row)
subset_row = df.iloc[[1,3],[0,1]]
print("\nvalue from the second and fourth row and first and second column :\n",subset_row)
