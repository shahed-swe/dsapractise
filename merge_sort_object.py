import random
import time
import string

def random_string(length=5):                                                                                                                                                                               
    # Generate a random string of fixed length                                                                                                                                                             
    letters = string.ascii_letters                                                                                                                                                                         
    return ''.join(random.choice(letters) for _ in range(length)) 


def merge(left_array, right_array, key):
    result = []
    i = j = 0

    while i < len(left_array) and j < len(right_array):
        if left_array[i][key] < right_array[j][key]:
            result.append(left_array[i])
            i += 1
        else:
            result.append(right_array[j])
            j += 1

    result.extend(left_array[i:])
    result.extend(right_array[j:])

    return result

def merge_sort(arr, key):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_array = merge_sort(arr[:mid], key)
    right_array = merge_sort(arr[mid:], key)

    return merge(left_array, right_array, key)


if __name__ == '__main__':
    random_objects = [
        {"id": random.randint(1, 100), "name": random_string()} for _ in range(50)
    ]
    start_time = time.time()
    new_sorted_list = merge_sort(random_objects, 'id')

    end_time = time.time()

    print(new_sorted_list)
    print(end_time - start_time)
    # print(random_objects)