n=str(input("Enter the numbers: "))
N=n.isnumeric()
if n!=N:
     print("Enter a valid number")
else:
    while(N>0):
        reverse=0
        a=N%10
        reverse= reverse*10+a
        N=N//10
    print(reverse)
