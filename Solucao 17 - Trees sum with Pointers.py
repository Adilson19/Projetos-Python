#target_sum = 0
#numbers = [-8, -6, -5, -2, 1, 2, 3, 5, 6, 12]
# Tempo: O(n2) - O(n)
def solution(numbers, target_sum):
    result = []
    sorted_numbers = list(sorted(numbers))

    for current in range(len(numbers)):
        left_pointer = current + 1
        right_pointer = len(numbers) - 1

        while left_pointer < right_pointer:
            pointers_sum = sorted_numbers[current]
            pointers_sum += sorted_numbers[left_pointer]
            pointers_sum += sorted_numbers[right_pointer]

            if pointers_sum == target_sum:
                left_pointer += 1
            elif pointers_sum < target_sum:
                right_pointer -= 1
            else:
                result.append([sorted_numbers[current], sorted_numbers[left_pointer], sorted_numbers[right_pointer]])

                left_pointer += 1
                right_pointer -= 1
    return result 