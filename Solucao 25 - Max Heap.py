class MaxHeap:
    def __init__(self, array):
        self.heap = self.build_heap(array)

    def build_heap(self, array):
        parent_index = (len(array) - 2) // 2
        for current_index in reversed(range(parent_index + 1)):
            self.sift_down(current_index, len(array) - 1, array)
        return array

    #Pegar o primeiro valor do Heap
    def peek(self):
        return self.heap[0]

    def sift_down(self, current_index, end_index, heap):
        left_child_index = (2 * current_index) + 1
        while left_child_index <= end_index:
            right_child_index = (2 * current_index) + 2

            # Determine qual filho é menor
            child_to_swap = left_child_index
            if right_child_index < len(heap) and heap[left_child_index] < heap[right_child_index]:
                child_to_swap = right_child_index

            if child_to_swap >= len(heap):
                break

            if heap[child_to_swap] < heap[current_index]:
                break
            else:
                self.swap(current_index, child_to_swap, heap)

            current_index = child_to_swap
            left_child_index = (2 * current_index) + 1

    def sift_up(self, current_index):
        parent_index = (current_index - 1) // 2
        while current_index > 0 and self.heap[current_index] > self.heap[parent_index]:
            self.swap(current_index, parent_index, self.heap)
            current_index = parent_index
            parent_index = (current_index - 1) // 2

    #Remove o valor maximo do heap
    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        value_to_remove = self.heap.pop()
        self.sift_down(0, len(self.heap) - 1, self.heap)
        return value_to_remove

    #Inserir um novo valor no heap (deve manter as propriedades validas)
    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1)

    def swap(self, index1, index2, heap):
        heap[index1], heap[index2] = heap[index2], heap[index1]