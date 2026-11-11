def solution(numbers, k):
    #   Criando o Hash_map
    hash_map = {}

    # O(n) - O(n)
    #   Pegando a frequencia de cada numero
    for num in numbers:
        if num not in hash_map:
            hash_map[num] = 0
        hash_map[num] += 1

    # {1: 3, 2: 1, 3: 2}

    # O(n log n) - O(n)
    #   Ordenando os pares pela frequencia
    pairs = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)

    # O(k) - O(k)
    result = []
    for pair in pairs[:k]:
        if pair[1] == k:
            result.append(pair[0])
    return result