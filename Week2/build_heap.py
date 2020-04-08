# python3


class HeapBuilder:
    """Converts an array of integers into a min-heap.
    A binary heap is a complete binary tree which satisfies the heap ordering
    property: the value of each node is greater than or equal to the value of
    its parent, with the minimum-value element at the root.
    Samples:
    >>> heap = HeapBuilder()
    >>> heap.array = [5, 4, 3, 2, 1]
    >>> heap.generate_swaps()
    >>> heap.swaps
    [(1, 4), (0, 1), (1, 3)]
    >>> # Explanation: After swapping elements 4 in position 1 and 1 in position
    >>> # 4 the array becomes 5 1 3 2 4. After swapping elements 5 in position 0
    >>> # and 1 in position 1 the array becomes 1 5 3 2 4. After swapping
    >>> # elements 5 in position 1 and 2 in position 3 the array becomes
    >>> # 1 2 3 5 4, which is already a heap, because a[0] = 1 < 2 = a[1],
    >>> # a[0] = 1 < 3 = a[2], a[1] = 2 < 5 = a[3], a[1] = 2 < 4 = a[4].
    >>> heap = HeapBuilder()
    >>> heap.array = [1, 2, 3, 4, 5]
    >>> heap.generate_swaps()
    >>> heap.swaps
    []
    >>> # Explanation: The input array is already a heap, because it is sorted
    >>> # in increasing order.
    """

    def __init__(self):
        self.swaps = []
        self.array = []

    @property
    def size(self):
        return len(self.array)

    def read_data(self):
        """Reads data from standard input."""
        n = int(input())
        self.array = [int(s) for s in input().split()]
        assert n == self.size

    def write_response(self):
        """Writes the response to standard output."""
        print(len(self.swaps))
        for swap in self.swaps:
            print(swap[0], swap[1])

    def l_child_index(self, index):
        """Returns the index of left child.
        If there's no left child, returns -1.
        """
        l_child_index = 2 * index + 1
        if l_child_index >= self.size:
            return -1
        return l_child_index

    def r_child_index(self, index):
        """Returns the index of right child.
        If there's no right child, returns -1.
        """
        r_child_index = 2 * index + 2
        if r_child_index >= self.size:
            return -1
        return r_child_index

    def sift_down(self, i):
        """Sifts i-th node down until both of its children have bigger value.
        At each step of swapping, indices of swapped nodes are appended
        to HeapBuilder.swaps attribute.
        """
        min_index = i
        l = self.l_child_index(i)
        r = self.r_child_index(i)

        if l != -1 and self.array[l] < self.array[min_index]:
            min_index = l

        if r != - 1 and self.array[r] < self.array[min_index]:
            min_index = r

        if i != min_index:
            self.swaps.append((i, min_index))
            self.array[i], self.array[min_index] = \
                self.array[min_index], self.array[i]
            self.sift_down(min_index)

    def generate_swaps(self):
        """Heapify procedure.
        It calls sift down procedure 'size // 2' times. It's enough to make
        the heap completed.
        """
        for i in range(self.size // 2, -1, -1):
            self.sift_down(i)

    def solve(self):
        self.read_data()
        self.generate_swaps()
        self.write_response()


if __name__ == "__main__":
    heap_builder = HeapBuilder()
    heap_builder.solve()