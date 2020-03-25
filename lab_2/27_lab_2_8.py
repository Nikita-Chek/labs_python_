import argparse
import math

def is_power_of2(n):
	if n == 0:
		return False
	return math.log(n, 2).is_integer()

def is_power_of2_chek(n):
	if n == 0:
		return False
	if n.is_integer():
		n = int(n)
		return n & (n-1) == 0
	return False

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--number', type=int, help='input non negative number')
parser.add_argument('-c','--chek', type=bool, help='True/False if you need to chek')
inputs = parser.parse_args()

n = inputs.number


if n is None or n < 0:
	print("input non negative number")
	n = -1
	while n < 0:
		n = int(input()) 

print(is_power_of2(n))

flag = inputs.chek
if flag:
	print(is_power_of2_chek(n))
