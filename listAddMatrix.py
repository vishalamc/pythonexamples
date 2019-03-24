list1=[
[1,2,3],
[4,5,6],
[7,8,9]
]
list2=[
[1,1,1],
[1,1,1],
[1,1,1]
]
result=[
[0,0,0],

[0,0,0],

[0,0,0]
]

for i in range(len(list1)):
 for j in range(len(list2)):
  result[i][j]=list1[i][j]+list2[i][j]

for k in result:
 print(k)

