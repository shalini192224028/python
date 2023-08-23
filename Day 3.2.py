N1=int(input("N1: "))
N2=int(input("N2: "))
N3=int(input("N3: "))
L=[]
L.append(N1)
L.append(N2)
L.append(N3)
print(L)
if N1<=0 or N2<=0 or N3<=0:
    print("Enter a positive number")
elif N1<10 and N2<10 and N3<10:
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if (i!=j and j!=k and i!=k):
                    print(L[i], L[j], L[k])
else:
    print("Enter a valid number")
