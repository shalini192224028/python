total_users=int(input("total users: "))
staff_users=int(input("staff users: "))
if (total_users<=0):
    print("Invalid input")
elif total_users==staff_users or total_users<staff_users:
    print("Invalid input")
else:
    non_teaching=staff_users/3
    student_users=total_users-(staff_users+non_teaching)
    n=int(student_users)
    print(n)
