# Write a Python program to print a specified list after removing the 0th, 2nd, 4th
# and 5th elements.
# remove()
# pop()
# del()

lst=[0,1,2,3,4,5,6,7,8]
print(lst)
# lst1 = [x for (i,x) in enumerate(lst) if i not in (0,2,4,5)]
# print(lst1)


# for i in lst:
# 	if i not in (0,2,4,5):
# 		print(i,end=" ")

lst1=[]
for i in lst:
	if i not in (0,2,4,5):
		lst1.append(i);
print(lst1)