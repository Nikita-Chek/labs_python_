import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--args', nargs='+', type=int)

list = parser.parse_args().args

list = [[2,3], [3, 'er'], [[4], 3], [[[6]]]]

def flatten(list):
	#fl = [val for sublist in list for val in sublist] 
	fl = []
	
	return fl

print(flatten(list))