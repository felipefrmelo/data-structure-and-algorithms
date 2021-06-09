import math
from copy import deepcopy


class MinHeap:

    def __init__(self, heap=[]) -> None:
        self.heap = deepcopy(heap)
        self.buildHeap()

    def buildHeap(self):
        for i in range(self.parent(self.tail), -1, -1):
            self.heapify(i)

    @property
    def tail(self):
        return len(self.heap) - 1

    @property
    def size(self):
        return len(self.heap)

    @property
    def is_empty(self) -> bool:
        return len(self.heap) == 0

    def left(self, index) -> int:
        return 2 * index + 1

    def right(self, index) -> int:
        return 2 * (index + 1)

    def parent(self, index) -> int:
        return math.floor((index-1)/2)

    def add(self, n):

        self.heap.append(n)
        index = self.tail
        while (self._parentIsGreater(index)):

            self._swap(index, self.parent(index))

            index = self.parent(index)

    def remove(self):
        if(self.is_empty):
            raise RuntimeError("Empty")

        self._swap(0, self.tail)
        removed = self.heap.pop()
        self.heapify(0)
        return removed

    def heapify(self, index):
        if(self._isLeaf(index) or not self._isValidIndex(index)):
            return

        index_min = self._min_index(index, self.left(index), self.right(index))
        if(index_min != index):
            self._swap(index, index_min)
            self.heapify(index_min)

    def _min_index(self, index, left, right):
        if (self.heap[index] < self.heap[left]):
            if (self._isValidIndex(right)):
                if (self.heap[index] > self.heap[right]):
                    return right
            return index
        else:
            if (self._isValidIndex(right)):
                if (self.heap[left] > self.heap[right]):
                    return right
            return left

    def _parentIsGreater(self, index):
        return index > 0 and self.heap[self.parent(index)] > self.heap[index]

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _isValidIndex(self, index):
        return index >= 0 and index <= self.tail

    def _isLeaf(self, index):
        return index > self.parent(self.tail) and index <= self.tail


class PriorityQueue:
    def __init__(self):
        self.heap = MinHeap()

    @property
    def size(self):
        return self.heap.size

    def enqueue(self, obj):
        self.heap.add(obj)

    def dequeue(self):
        return self.heap.remove()

    def __repr__(self) -> str:
        return "[" + ','.join([f"{value}" for value in self.heap.heap]) + "]"
