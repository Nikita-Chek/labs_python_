import string
import os

def merge_sort(array):
    n = len(array)
    if n < 2:
        return array

    left = merge_sort(array[0:n//2])
    right = merge_sort(array[n//2:n])

    i = j = 0
    sort_array = []
    while (i < len(left)) or (j < len(right)):
        if i >= len(left):
            sort_array.append(right[j])
            j += 1
        elif j >= len(right):
            sort_array.append(left[i])
            i += 1
        elif left[i] < right[j]:
            sort_array.append(left[i])
            i += 1
        else:
            sort_array.append(right[j])
            j += 1

    return sort_array


file = open('additional/sort.txt','r')
string = file.read().split('\n')
file.close()
length = len(string)




for _ in range(length):
	string[_] = sorted(string[_].split())
	string[_] = list(string[_])
	for x in range(len(string[_])):
		string[_][x] = sorted(list(string[_][x]))
print(string)