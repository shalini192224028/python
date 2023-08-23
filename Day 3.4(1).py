a=input("bin1: ")
b=input("bin2: ")
if (a,b)!=(0,1):
    print("Enter a valid number")
sum=bin(int(a,2)+ int(b,2))
print(sum[2: ])
