import pandas as pa
data={
    'Product':['Pen','Nootbook','Eraser'],
    'Price':[20,21,22],
    'Stock':[100,200,300]
}
df=pa.DataFrame(data)
print("Data Dictionary: ")
print("---------------------------------------")
print(df)
print("---------------------------------------")
df['Discounted']=df['Price']*0.9
print("Data Dictionary with Discounted Price: ")
print("---------------------------------------")
print(df)
print("---------------------------------------")