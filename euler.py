# Project Euler 1
def euler(number):
	solution = []
	for i in range (0, number):
		if i % 3 == 0 or i % 5 == 0:
			solution.append(i);
	print('Euler Solution is:', sum(solution))

euler(1000);