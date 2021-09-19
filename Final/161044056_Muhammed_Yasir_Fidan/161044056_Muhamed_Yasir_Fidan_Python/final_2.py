
import math

def create_table(arr):
    table = [[0 for x in range(math.floor(math.log2(len(arr)))+1)] for y in range(len(arr))]
    for i in range(len(arr)):
        table[i][0] = i
    j = 1
    while len(arr) >= pow(2,j):
        i = 0
        while i+pow(2,j)-1 < len(arr):
            if(arr[table[i+pow(2,j-1)][j-1]] > arr[table[i][j-1]]):
                table[i][j] = table[i][j-1]
            else:
                table[i][j] = table[i+pow(2,j-1)][j-1]

            i += 1

        j += 1
    return table

def interval(arr,a,b,table):
    size = b-a+1
    k = math.floor(math.log2(size))
    return min(arr[table[a][k]],arr[table[a+size-pow(2,k)][k]])


def find_mins(x,intervals):
    table = create_table(x)
    for i in range(len(intervals)):
        result = interval(x,intervals[i][0]-1,intervals[i][1]-1,table)
        print(f'[{intervals[i][0]},{intervals[i][1]}] min = {result}')

x = [4,6,1,5,7,3]
intervals = [[1,5],[3,4],[5,5],[4,6],[2,6],[1,6]]
find_mins(x,intervals)
