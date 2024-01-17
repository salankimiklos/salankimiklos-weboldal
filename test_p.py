print('Fibonacci numbers program\n')
a=0
b=1
print('Numbers to display: ')
n=int(input())
for i in range(n):
	c=a+b
	a=b
	b=c
	print(c,' ')