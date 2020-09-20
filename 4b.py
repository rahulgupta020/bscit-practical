'''Write a Python program to print a specified list after removing the 0th, 2nd, 4th
and 5th elements.'''

lst=[0,1,2,3,4,5,6,7,8]
print("Original List :- ", lst)

newlist=[]
for i in lst:
	if i not in (0,2,4,5):
		newlist.append(i)
print(newlist)
