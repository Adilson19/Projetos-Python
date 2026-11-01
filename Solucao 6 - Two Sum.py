#target = 9
#array = [4, 1, 2, -2, 11, 15, 1, -1, -6, -4]

#for i in range(len(target)):
    #for j in range(i + 1, len(target)):

def solution(numbers, target_sum):
    for number1_index in range(len(numbers)):
        number1 = numbers[number1_index]

    for number2_index in range(number1_index + 1, len(numbers)):
        if number1 + numbers[number2_index] == target_sum:
            return [number1, numbers[number2_index]]
    return []