class Queue:
    # constructor
    def __init__(self, limit=10):
        self.data = [None] * limit
        self.head = -1
        self.tail = -1
        self.max_size = limit
        self.size = 0

    # adds a value to the queue
    def enqueue(self, val):
        # size validation
        if self.size == self.max_size:
            raise RuntimeError

        if self.head < 0:  # 0 case, first item
            self.head = self.tail = 0
        else:  # other case
            self.tail = (self.tail + 1) % self.max_size

        # size logic
        self.size += 1

        # assign value
        self.data[self.tail] = val

    # removes a value from the queue
    def dequeue(self):
        # check size
        if self.size == 0:
            raise RuntimeError

        # value logic
        val = self.data[self.head]
        self.data[self.head] = None

        # index logic
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        if self.data[self.head] is None:
            self.head = self.tail = -1

        return val

    # resizes the queue
    def resize(self, new_size):
        # assertion to make sure new size is less than current size
        assert (len(self.data) < new_size)

        # init new queue
        new_data = [None] * new_size

        # move items
        for idx in range(self.head, self.tail + self.max_size + 1):
            new_data[idx % new_size] = self.data[idx % self.max_size]

        # change variables
        self.tail = (self.tail + self.max_size) % new_size
        self.data = new_data
        self.max_size = new_size

    # checks if the queue is empty
    def empty(self):
        for val in self.data:
            if val is not None:
                return False
        return True

    # true if the queue is not empty
    def __bool__(self):
        return not self.empty()

    # returns length of queue
    def __len__(self):
        return self.size

    # string containing elements of queue
    def __str__(self):
        if not self:
            return ''
        return ', '.join(str(x) for x in self)

    # representation of queue (same as str)
    def __repr__(self):
        return str(self)

    # iterator for the queue
    def __iter__(self):
        idx = self.head
        for _ in range(self.size):
            if self.data[idx] is not None:
                yield self.data[idx]
            idx = (idx + 1) % self.size
