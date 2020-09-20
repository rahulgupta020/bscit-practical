'''Write a program that takes two lists and returns True if they have at least one
common member'''

lst1=[1,2,3,4,5]
lst2=[5,6,7,8,9]
for x in lst1:
	for y in lst2:
		if(x==y):
			print("True")