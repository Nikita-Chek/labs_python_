import argparse
import json
import os

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str)
file = parser.parse_args().file

with open('additional/array_json.json', 'r') as f:
	data = json.load(f)

List = data[""]
#[[2,3], [3, 'er'], [[4], [3,['t',[6,['qw'],5,2]]]], [[[6]]]]

def flatten(List, fl = []):
	for _ in range(len(List)):
		if type(List[_]) is list:
			flatten(List[_], fl)
		else:
			fl.append(List[_])
	return fl

print(flatten(List))
