test_list = [5, 6, 2, 5, 3, 3, 6, 5, 5, 6, 5]

print("The original list : " + str(test_list))

res = sorted(set(test_list), key = lambda ele: test_list.count(ele))
 
print("The list after sorting and removal : " + str(res))
