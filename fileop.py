import sys
print("Enter the data")
data = sys.stdin.read()   # Use Ctrl d to stop the input
print(data)
strfile=input("Enter a file a name")
filename ="D:/fileEx/"+strfile+".txt"
fileobj=open(filename,"w")
print("file created")
strcontent=input("Enter content of file")
fileobj.write(strcontent)
print("done")
fileobj.close()
fileobj1=open(filename,"r")
print("File contents are:")
strdata=fileobj1.readline()
print(strdata)
fileobj.close()
