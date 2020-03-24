#sqrt_decomposition

import sys
import argparse
import math

# array = input("input array: ").split()
# start = int(input("start: "))
# end = int(input("end: "))

parser = argparse.ArgumentParser()

parser.add_argument('-a', '--args', nargs='+', type=int)
parser.add_argument('-s', type=int)
parser.add_argument('-e', type=int)
parser.add_argument('-c', type=bool)

array = parser.parse_args().args
start = parser.parse_args().s
end = parser.parse_args().e
flag = False
flag = parser.parse_args().c

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

def sum_chek(array, start, end):
	sum = 0
	for x in range(start, end+1):
		sum += array[x]
	return sum


print(sum(array, start, end))
if flag:
	print(sum_chek(array, start, end))
