def is_sorted(array, index):
    if index == 0:
        return array[index] <= array[index + 1]
    if index == len(array) - 1:
        return array[index - 1] <= array[index]

    return array[index - 1] <= array[index] and array[index + 1] >= array[index]

def solution(array):
    max_number = float('-inf')
    min_number = float('inf')

    # -inf -> 5
    found = False
    for index in range(0, len(array)):
        if not is_sorted(array, index):
            max_number = max(array[index], max_number)
            min_number = min(array[index], min_number)
    if min_number == float('inf'):
        return [-1, -1]

    min_index = 0
    while min_number >= array[min_index]:
        min_index += 1

    max_index = len(array) - 1
    while max_number <= array[max_index]:
        max_index -= 1

    return [min_index, max_index]
