#Write a program to generate the Fibonacci series.

n=int(input("Enter a number :- "))
first=0
second=1
for i in range(n):
	print(first)
	temp=first
	first=second
	second = second+temp