# Write a program that takes two lists and returns True if they have at least one
# common member.

def common(lst1,lst2):
	for x in lst1:
		for y in lst2:
			if(x==y):
				return True

lst1=[1, 2, 3, 4, 5]
lst2=[51, 6, 7, 8, 9]
if common(lst1,lst2)==True:
	print('t')
else:
	print('f')


# lst1=[1, 2, 3, 4, 5]
# lst2=[5, 6, 7, 8, 9]
# aset=set(lst1)
# bset=set(lst2)
# if(aset & bset):
# 	print("Yes")
# else:
# 	print("No")