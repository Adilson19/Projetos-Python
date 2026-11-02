#target = 9
#array = [4, 1, 2, -2, 11, 15, 1, -1, -6, -4]
#array = [-6, -4, -2, -1, 1, 1, 2, 4, 11, 16]

def solution(numbers, target_sum):
    numbers.sort()

    left_pointer = 0
    right_pointer = len(numbers) - 1

    while left_pointer < right_pointer:
        numbers_sum = numbers[left_pointer] + numbers[right_pointer]
        if numbers_sum == target_sum:
            return [numbers[left_pointer], numbers[right_pointer]]
        elif numbers_sum < target_sum:
            left_pointer += 1
        elif numbers_sum > target_sum:
            right_pointer -= 1
    return []
print(solution([-6, -4, -2, -1, 1, 1, 2, 4, 11, 16], 9))