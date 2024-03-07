import random
import time

def merge(left, right):
    result = []
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def merge_sort(arr):
    if(len(arr) <= 1):
        return arr

    mid = len(arr) // 2
    left_array = merge_sort(arr[:mid])
    right_array = merge_sort(arr[mid:])

    return merge(left_array, right_array)


if __name__ == '__main__':
    start_time = time.time()
    sortedlist = merge_sort([random.randint(1, 200) for _ in range(100)])
    end_time = time.time()

    print(end_time - start_time)
    print(sortedlist)
