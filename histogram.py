'''Define a procedure histogram() that takes a list of integers and prints a
histogram to the screen. For example, histogram([4, 9, 7]) should print the
following:
****
*********
*******
'''
def histogram(lst):
	for i in lst:
		print(i * '*')

lst=[]
ln=int(input("Enter the list length :- "))
print("Enter interger = ",ln)
for i in ln:
	data = int(input())
	lst.append(data)

histogram(lst)

















def histogram(lst):
	for i in lst:
		print(i * '*')

lst=[]
ln=int(input("Enter the list length :- "))
print("Enter interger ",ln)
for i in range(ln):
	data = int(input())
	lst.append(data)

histogram(lst)