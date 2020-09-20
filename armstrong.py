# while(temp>0):
# remainder=temp%10
# result=remainder**3+result
# temp=temp/10

# if(result==n)

n=int(input("Enter a number :- "))
temp=n
result=0
while(temp!=0):
	remainder=temp%10
	result=remainder**3+result
	temp=temp//10

if(result==n):
	print(result, " is an armstrong number ")
else:
	print(result, " is not an armstrong number ")

