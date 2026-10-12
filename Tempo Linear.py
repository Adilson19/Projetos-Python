def print_items(my_array):
    for item in my_array:
        print(item)

def find_max(my_array):
    max = 0
    for item in my_array:
        if item > max:
            max = item
    return max

def find_sum(my_array):
    sum = 0
    for item in my_array:
        sum += item
    return sum
