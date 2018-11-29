# problem_1
sum_total = 0
num_3 = 0
num_5 = 0
number =1000
for i in range(number):
	if (num_3+3 < number):
		num_3 = num_3 + 3
		print(num_3)
		sum_total = sum_total + num_3
	if (num_5 + 5 < number):
		num_5 = num_5 + 5
		print(num_5)
		sum_total = sum_total + num_5 
	if (num_3+3 >= number and num_5 + 5 >= number):
		print(num_3)
		print(num_5)
		break

print(sum_total)		
