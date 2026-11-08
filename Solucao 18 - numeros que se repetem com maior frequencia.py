def solution(numbers, k):
    hash_map = {}

    # O(n) - O(n)
    for num in numbers:
        if num not in hash_map:
            hash_map[num] = 0
        hash_map[num] += 1

    # {1: 3, 2: 1, 3: 2}

    # O(nlogn) - O(n)
    pairs = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)

    result = []
    for pair in pairs[:k]:
        if pair[1] == k:
            result.append(pair[0])
    return result