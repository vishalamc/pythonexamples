import pandas as pd
list=["kumar","Raj","vishal"]
disct={"key1":"value1","key2":"value2","key3":123}
s = pd.Series(list)
#s=pd.Series(disct)
print(s)
print(s[1])
#print(s["key2"])
