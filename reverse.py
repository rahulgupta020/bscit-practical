#Write a function that reverses the user defined value.

# while(n>0)
# reminder=n%10
# reverse=(reverse*10)+reminder
# n=n/10

def rev(n):
	reverse=0
	while(n>0):
		reminder=n%10
		reverse=(reverse*10)+reminder
		n=n//10
	return reverse
n=int(input("Enter a number :- "))
reverse1=rev(n)
print("reverse number is :- ", reverse1)





# n=int(input("Enter a number :- "))
# reverse=0
# while(n>0):
# 	reminder=n%10
# 	reverse=(reverse*10)+reminder
# 	n=n//10

# print("reverse number is :- ", reverse)