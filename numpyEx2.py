import numpy as np
num=np.array([2,1,3,5,4,6])
print("Unsorted elements are:")
print(num)
print("sorted elements are:")
temp=0
for i in range(0,num.size):
    if(num[i]>num[i+1]):
        temp=num[i+1]
        num[i+1]=num[i]
        num[i]=temp
        
    print(num[i])
