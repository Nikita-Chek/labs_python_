import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--number', type=int)
parser.add_argument('-c','--chek', type=bool)
n = int(parser.parse_args().number)
if n < 0:
	print("input non negative number")

while n < 0:
	print("non negative number")
	n = int(input())

flag = False
flag = parser.parse_args().chek

fi = (1 + math.sqrt(5)) / 2
psi = (1 - math.sqrt(5)) / 2


def leonardo_number(n):
	if n == 0:
		return 1
	if n == 1:
		return 1
	return leonardo_number(n-1) + leonardo_number(n-2) + 1  

def fibonacci(n):
	return int((fi**n - psi**n) / math.sqrt(5))

def leonardo_chek(n):
	return 2 * fibonacci(n+1) - 1

print(leonardo_number(n))

if flag:
	print(leonardo_chek(n))