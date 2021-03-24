class Heap:
    # init heap
    def __init__(self, key=lambda x: x):
        self.data = []
        self.key = key

    # static methods
    @staticmethod
    def _parent(idx):
        return (idx - 1) // 2

    @staticmethod
    def _left(idx):
        return idx * 2 + 1

    @staticmethod
    def _right(idx):
        return idx * 2 + 2

    # heapify
    def heapify(self, idx=0):
        while True:
            # get indexes
            left_node = Heap._left(idx)
            right_node = Heap._right(idx)
            max_idx = idx

            # set max_idx logic
            if left_node < len(self.data) and self.key(self.data[left_node]) > self.key(self.data[max_idx]):
                max_idx = left_node
            if right_node < len(self.data) and self.key(self.data[right_node]) > self.key(self.data[max_idx]):
                max_idx = right_node

            # check if swap is needed
            if max_idx == idx:
                break
            else:
                # swap max_idx with idx
                self.data[max_idx], self.data[idx] = self.data[idx], self.data[max_idx]
                idx = max_idx

    # add to heap
    def add(self, x):
        # put data at the end
        self.data.append(x)

        # init indexes
        idx = len(self.data) - 1
        parent = Heap._parent(idx)

        # sort heap
        while idx > 0 and self.key(self.data[parent]) < self.key(self.data[idx]):
            self.data[parent], self.data[idx] = self.data[idx], self.data[parent]
            idx = parent
            parent = Heap._parent(idx)

    # peek at front of heap
    def peek(self):
        return self.data[0]

    # pop from front of heap
    def pop(self):
        ret = self.data[0]
        self.data[0] = self.data[len(self.data) - 1]
        del self.data[len(self.data) - 1]
        self.heapify()
        return ret

    # return true if heap is not empty
    def __bool__(self):
        return len(self.data) > 0

    # return length of heap
    def __len__(self):
        return len(self.data)

    # return representation of heap
    def __repr__(self):
        return repr(self.data)
