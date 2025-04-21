import numpy as np
from scipy import stats as st
arr=np.array([12,15, 12, 18, 21, 24, 24, 24, 27, 30])
print("Original array:",arr)
print("Mean: ",np.mean(arr))
print("Median: ",np.median(arr))    
print("Standard deviation: ",np.std(arr))
print("Variance: ",np.var(arr))
print("Mode: ",st.mode(arr))