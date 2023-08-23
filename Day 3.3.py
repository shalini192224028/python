def goodpairs(num):
    count=0
    n=len(num)
    print("length",n)
    for i in range(n):
        for j in range(i+1,n):
            print("i",num[i],"j",num[j],"pos i", i, "pos j",j)
            if num[i]==num[j]and i<j:
                count+=1
    return count

num=[1,1,1,1]
print("Output: ",goodpairs(num))
