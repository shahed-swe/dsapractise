import random
import time


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    start_time = time.time()
    sortedlist = quicksort([random.randint(1, 200) for _ in range(100)])
    end_time = time.time()

    print(end_time - start_time)
    print(sortedlist)
