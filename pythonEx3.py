import pandas as pd
import matplotlib.pyplot as pt
dict={
    'player':["A","B","C"],
    'Age':[10,20,30]
    }
df=pd.DataFrame(dict)
print(df)
df.plot(x='player',y='Age',kind='bar')
pt.show()
