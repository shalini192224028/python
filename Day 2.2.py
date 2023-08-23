n=input("Enter the year ")
if n.isdigit() and int(n):
    n=int(n)
    if (n<=0):
        ptint("Enter a valid number")
    elif (n%400==0)and(n%100!=0):
        print("It ia a leap year")
    elif (n%4==0):
        print("It is a leap year")
    else:
        print("It is not a leap year")
else:
    print("It is not a leap year")
    
