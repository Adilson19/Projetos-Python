import heapq

heapq = [1, 2, 65, 78, 98, 3, 6, 7, 99]

heapq.heapify(heapq)
heapq

heapq.nlargest(3, heapq)

heapq.nsmallest(3, heapq)