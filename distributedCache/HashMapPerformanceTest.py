import time
import sys

hm1 = {}
numElements = 999999999

print('Starting Single HashMap Test')

for i in range(numElements):
    setStartTime = time.time()
    hm1[i] = str(i)
    setEndTime = time.time()

    if i % 10000000 == 0:
        getStartTime = time.time() 
        value = hm1[i]
        getEndTime = time.time()

        getSizeStartTime = time.time()
        size = sys.getsizeof(hm1) / 1000000.0
        getSizeEndTime = time.time()

        print(f'Value: {i} | setTime: {setEndTime - setStartTime} | getTime: {getEndTime - getStartTime} | HashMapSize: {size} MB | getSizeTime: {getSizeEndTime - getSizeStartTime}')
