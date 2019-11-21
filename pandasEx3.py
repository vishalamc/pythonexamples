import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
df = pd.DataFrame(np.random.rand(10, 3), columns =['a', 'b', 'c']) 
  
print(df)

df.plot.bar() 
plt.show()
