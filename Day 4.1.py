n=int(input("enter a number"))
l=[]
k=str(l)
for i in range (1,n+1):
    if (i%3==0):
        l.append("fuzz")
    elif(i%5==0):
        l.append("Buzz")
    else:
        j=i
        l.append(str(i))
print(l)
