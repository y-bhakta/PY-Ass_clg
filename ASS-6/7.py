import pandas as pa
data={
    'Product':['Pen','Nootbook','Eraser'],
    'Price':[20,21,22],
    'Stock':[100,200,300]
}
print("Data Dictionary: ")
print("---------------------------------------")
print(pa.DataFrame(data))