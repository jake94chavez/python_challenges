# FizzBuzz
def fizzbuzz(number):
	for i in range (1, number):
		if i % 15 == 0:
			print('Fizzbuzz');
		elif i % 3 == 0:
			print('Fizz');
		elif i % 5 == 0:
			print('Buzz');
		else:
			print(i);

fizzbuzz(100);

# Fibonacci
def fib(number):
	fib_list = [0, 1]
	for i in range (1, number):
		fib_list.append(fib_list[i]+fib_list[(i-1)])
	print('Fibbonaci sequence number at position', number, 'is', fib_list[number])

fib(6)

# Project Euler 1
def euler(number):
	solution = []
	for i in range (0, number):
		if i % 3 == 0 or i % 5 == 0:
			solution.append(i);
	print('Euler Solution is:', sum(solution))

euler(1000);