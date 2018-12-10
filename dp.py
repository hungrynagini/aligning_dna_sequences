import math
import time
import random
import numpy
start_time = time.time()


def configure_param(a, b):
    if len(a) > len(b):
        a, b = b, a
    return a, b


def xdrop(x, ind, mat, mis, a, b):
    a, b = configure_param(a, b)
    len_a = len(a)
    print(len_a)
    len_b = len(b)
    print(len_b)
    max_length = max(len_a, len_b)
    align_matrix = [[None for i in range(max_length*4+1)]for j in range(max_length*4+1)]
    align_matrix[0][0], diagonal, lower, upper, t, tt = 0, 0, 0, 0, 0, 0
    while lower <= upper+2:
        diagonal += 2
        for i in range(math.ceil(lower), (math.floor(upper)+3)):
            # this condition was added to insure that the last matching elements are found
            if lower > upper:
                upper, lower = lower, upper
            if lower == upper:
                lower -= 1
                upper += 2
            j = diagonal - i
            align_matrix[i][j] = float('-inf')
            if i % 2 == 0:
                if (lower <= i <= upper+2) and a[int(i/2)-1] == b[int(j/2)-1] and i > 0 and j > 0:
                    if align_matrix[i - 1][j - 1] is not None:
                        align_matrix[i][j] = align_matrix[i - 1][j - 1] + mat / 2
                if lower <= i <= upper+2 and a[int(i/2)-1] != b[int(j/2)-1] and i > 0 and j > 0:
                    if align_matrix[i - 1][j - 1] is not None:
                        align_matrix[i][j] = max(align_matrix[i - 1][j - 1] + mis / 2, align_matrix[i][j])
                if 0 < i <= upper and j > 1:
                    if align_matrix[i][j - 2] is not None:
                        align_matrix[i][j] = max(align_matrix[i][j - 2] + ind, align_matrix[i][j])
                if lower <= i - 2 and i > 1 and j > 0:
                    if align_matrix[i - 2][j] is not None:
                        align_matrix[i][j] = max(align_matrix[i - 2][j] + ind, align_matrix[i][j])
            else:
                if a[int(i/2)] == b[int(j/2)]:
                    if align_matrix[i - 1][j - 1] is not None:
                        align_matrix[i][j] = align_matrix[i - 1][j - 1] + mat / 2

                else:
                    if align_matrix[i - 1][j - 1] is not None:
                        align_matrix[i][j] = align_matrix[i - 1][j - 1] + mis / 2
            tt = max(tt, align_matrix[i][j])
            if align_matrix[i][j] < t - x:
                align_matrix[i][j] = float('-inf')
        lst = [i for i in range(diagonal+1) if align_matrix[i][diagonal-i] and align_matrix[i][diagonal-i] > float("-inf")]
        if not lst:
            return "With "+str(x)+" as x could not find a sequence match"
        upper = max(lst)
        lower = min(lst)
        lower = max(lower, diagonal + 2 - 2*len_b)
        upper = min(upper, 2*len_a - 2)
        t = tt
    return tt


with open('one.txt', 'r') as file:
    file = ''.join(file.read().split())
with open("one.txt", 'r') as file1:
    file1 = ''.join(file1.read().split())
file = list(file)
file1 = list(file1)
for i in range(len(file)):
    if not i % 6:
        file[i] = random.choice(['a', 'c', 'g', 't'])
    if not i % 10:
        file[i] = random.choice([file[i], ''])
file = [i for i in file if i]
res = xdrop(100, -4, 4, -2, file, file1)
print('result = ', res)
print('execution time: ', time.time() - start_time)
