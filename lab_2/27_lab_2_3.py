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
	string[_] = string[_].split()
	string[_] = merge_sort(string[_])
string = merge_sort(string)


for _ in range(length):
    string[_] = ' '.join(string[_])


file = open('additional/sorted.txt','w')
for _ in string:
    file.write(_ + '\n')
file.close()
