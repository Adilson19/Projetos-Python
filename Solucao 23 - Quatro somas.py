#   target_sum = 16
#   numbers = [7, 6, 4, -1, 1, 2]
import array

def solution(numbers, target_sum):
    result = []
    hash_table = {13: [7, 6], 8: [4, 4]}

    for pointer in range(len(numbers)):
        for forward_pointer in range(pointer + 1, len(numbers)):
            my_sum = numbers[pointer] + numbers[forward_pointer]
            diff = target_sum - my_sum
            if diff in hash_table:
                for hash_sum in hash_table[diff]:
                    result.append(hash_sum + [array[pointer], array[forward_pointer]])

        for previous_pointer in range(pointer):
            my_sum = numbers[previous_pointer] + array[pointer]
            if my_sum not in hash_table:
                hash_table[my_sum] = []
            hash_table[my_sum].append([array[previous_pointer], array[pointer]])
    
    return result