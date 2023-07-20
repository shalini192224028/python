def plusOne(digits):
    n=len(digits)-1
    while digits[n]==9:
        digits[n]=0
        n=n-1
    if n<0:
        digits=[1]+digits
    else:
        digits[n]=digits[n]+1
    return digits
digits=[1,2,5,7]
print(plusOne(digits))
