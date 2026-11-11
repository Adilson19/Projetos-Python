# k = 2
# numbers = [1, 2, 3, 1, 2, 2, 4]
import heapq
#   O(n log k) -> O(n)
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

    # O(n log k) - O(n)
    #   Ordenando os pares pela frequencia
    heap = []
    for num, count in hash_map.items():
        heapq.heappush(heap, (count, num))
        if len(heap) > k:
            heapq.heappop(heap)

    # O(k) - O(k)
    result = []
    for pair in heap:
        result.append(pair[1])
    return result