# Fibonacci
def fib(number):
	fib_list = [0, 1]
	for i in range (1, number):
		fib_list.append(fib_list[i]+fib_list[(i-1)])
	print('Fibbonaci sequence number at position', number, 'is', fib_list[number])

fib(6)