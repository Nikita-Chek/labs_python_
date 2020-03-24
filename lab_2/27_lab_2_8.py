import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--number', type=float)
parser.add_argument('-c','--chek', type=bool)
n = parser.parse_args().number
if n < 0:
	print("input non negative number")

while n < 0:
	print("non negative number")
	n = int(input())

flag = False
flag = parser.parse_args().chek



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
print(is_power_of2(n))
if flag:
	print(is_power_of2_chek(n))
