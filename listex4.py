alpha=0
digit=0
str=input("Enter string")
for i in range(0,len(str)):
	if(str[i].isalpha()==True):
 		alpha=alpha+1
	if(str[i].isdigit()==True):
 		digit=digit+1
print("total letter",alpha)
print("total digit",digit)
