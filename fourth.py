#Write a function that reverses the user defined value.

n=int(input("Enter a number :- "))

reverse=0
while(n>0):
	reminder=n%10
	reverse=(reverse*10)+reminder
	n=n//10
print("Reverse number is = ",reverse)