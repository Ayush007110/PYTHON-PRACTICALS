f=open("file1.txt",'r')
count=0
for i in f:
    count=count+1
print(count)
f.close()