#sqrt_decomposition

import math

array = input("input array: ").split()
start = int(input("start: "))
end = int(input("end: "))

for _ in range(len(array)):     #from input string array to int array
	array[_] = int(array[_])

def sum(array, start, end):
	sum = 0
	length = len(array)
	n_length = int(math.ceil(math.sqrt(length)))
	n_array = [0 for _ in range(n_length)]

	for _ in range(length):				#sums of blocks
		n_array[_ // n_length] += array[_] 

	while start <= end:
		if (start % n_length == 0) and (start + n_length-1 <= end):
			sum += n_array[start // n_length]
			start += n_length;
		else:
			sum += array[start]
			start += 1
	return sum


print(sum(array, start, end))