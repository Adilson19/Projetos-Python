#   Tempo: O(n) - Espaco: O(1)
def solution(numbers, k):
    left_pointer = 0
    for right_pointer in range(len(numbers)):
        k -= 1 - numbers[right_pointer]
        if k < 0:
                k += 1 - numbers[left_pointer]
                left_pointer += 1
    return right_pointer - left_pointer + 1