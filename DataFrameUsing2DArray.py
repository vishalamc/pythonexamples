import pandas as pd
import numpy as np


arr2d=np.array([["kumar","Raj","Rohan"],[1001,1002,1003]])
df=pd.DataFrame(arr2d,index=['Name','Id'],columns =['Col1', 'Col2','Col3'])
print(df)


