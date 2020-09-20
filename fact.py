#Write a recursive function to print the factorial for a given number.

# def fact(n):
#     if(n==1):
#         return 1
#     else:
#        return n*fact(n-1)

def fact(n):
	if(n==1):
		return 1
	else:
		return n*fact(n-1)

n=int(input("Enter a number :- "))
result=fact(n)
print(result)