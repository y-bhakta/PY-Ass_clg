import numpy as np
from scipy import stats as st
l = [1,2,3,4,5,6,7,8,9,10]
print("List: ",l)
arr=np.array(l)
print("Original array:",arr)
print("Mean: ",np.mean(arr))
print("Median: ",np.median(arr))    
print("Standard deviation: ",np.std(arr))
print("Variance: ",np.var(arr))
print("Mode: ",st.mode(arr))