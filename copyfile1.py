file1=open("d:/hello.txt","w")
print("file created")
file1.write("hello my name is kumar")
print("content created")
file1.close()
file2=open("d:/hello2.txt","w")
print("2nd file created")
file3=open("d:/hello.txt","r")
for i in file3:
  file2.write(i)
print("2nd file copied")
file2.close()
file3.close()
