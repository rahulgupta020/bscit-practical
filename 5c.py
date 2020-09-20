#Write a Python program to sum all the items in a dictionary

#Method2
dic2 = {'python':90, 'cpp':100, 'java':80, 'php':50}
print(sum(dic2.values()))

#Method1
dic1 = {'python':90, 'cpp':100, 'java':80, 'php':50}
sum=0
for i in dic1.values():
	sum=sum+i
print(sum)

print()



