#   O(n) - O(n)
def solution(numbers, k):
    hash_map = {}
# O(n) - O(n)
    for number in numbers:
        if number not in hash_map:
            hash_map[number] = 0
        hash_map[number] += 1

# Pegando a frequencia de cada numberero
# {1: 3, 2: 1, 3: 2}
#   O(n) - O(n)
    frequency = {}
# Ordenando os pares pela frequencia
    for number, count in hash_map.items():
        if count not in frequency:
            frequency[count] = []
        frequency[count].append(number)
#   O(n)
    result = []
    for number in reversed(range(1, len(numbers) + 1)):
        if number in frequency:
            result.extend(frequency[number])
    return result[:k]
