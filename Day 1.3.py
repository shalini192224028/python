def ishappy(n):
    n1=set()
    while n != 1:
        n=(sum(int(i)**2 for i in str(n)))
        if n in n1:
            return False
        n1.add(n)
    return True           
               
n=int(input("Enter a number: "))
if n<=0 :
    print("Enter a positive integer")
elif n>0:
    print(ishappy(n))
