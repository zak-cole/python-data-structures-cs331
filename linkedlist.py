class LinkedList:
    class Node:
        def __init__(self, val, prior=None, next=None):
            self.val = val
            self.prior = prior
            self.next = next

    def __init__(self):
        self.head = LinkedList.Node(None)  # sentinel node (never to be removed)
        self.head.prior = self.head.next = self.head  # set up "circular" topology
        self.length = 0

    ### prepend and append, below, from class discussion

    def prepend(self, value):
        self.head = LinkedList.Node(value, self.head)
        n = LinkedList.Node(value, prior=self.head, next=self.head.next)
        self.head.next.prior = self.head.next = n
        self.length += 1

    def append(self, value):
        n = LinkedList.Node(value, prior=self.head.prior, next=self.head)
        n.prior.next = n.next.prior = n
        self.length += 1

    ### subscript-based access ###

    def _normalize_idx(self, idx):
        nidx = idx
        if nidx < 0:
            nidx += len(self)
            if nidx < 0:
                nidx = 0
        return nidx

    def __getitem__(self, idx):
        """Implements `x = self[idx]`"""
        assert (isinstance(idx, int))

        # normalize index
        nidx = self._normalize_idx(idx)

        # check length stuff
        if nidx < 0 or nidx > self.length:
            raise IndexError

        # iterate through nodes
        node = self.head.next
        for _ in range(nidx):
            node = node.next

        return node.val

    def __setitem__(self, idx, value):
        """Implements `self[idx] = x`"""
        assert (isinstance(idx, int))

        # normalize index
        nidx = self._normalize_idx(idx)

        # check length stuff
        if nidx < 0 or nidx > self.length:
            raise IndexError

        # iterate through nodes
        node = self.head.next
        for _ in range(nidx):
            node = node.next

        node.val = value

    def __delitem__(self, idx):
        """Implements `del self[idx]`"""
        assert (isinstance(idx, int))

        assert (isinstance(idx, int))

        # normalize index
        nidx = self._normalize_idx(idx)

        # check length stuff
        if nidx < 0 or nidx > self.length:
            raise IndexError

        # iterate through nodes
        node = self.head.next
        for _ in range(nidx):
            node = node.next

        node.prior.next = node.next
        node.next.prior = node.prior
        self.length -= 1

    ### cursor-based access ###

    def cursor_get(self):
        """retrieves the value at the current cursor position"""
        assert self.cursor is not self.head

    def cursor_set(self, idx):
        """sets the cursor to the node at the provided index"""

    def cursor_move(self, offset):
        """moves the cursor forward or backward by the provided offset
        (a positive or negative integer); note that it is possible to advance
        the cursor by further than the length of the list, in which case the
        cursor will just "wrap around" the list, skipping over the sentinel
        node as needed"""
        assert len(self) > 0

    def cursor_insert(self, value):
        """inserts a new value after the cursor and sets the cursor to the
        new node"""

    def cursor_delete(self):
        """deletes the node the cursor refers to and sets the cursor to the
        following node"""
        assert self.cursor is not self.head and len(self) > 0

    ### stringification ###

    def __str__(self):
        """Implements `str(self)`. Returns '[]' if the list is empty, else
        returns `str(x)` for all values `x` in this list, separated by commas
        and enclosed by square brackets. E.g., for a list containing values
        1, 2 and 3, returns '[1, 2, 3]'."""
        return '[' + ', '.join(str(x) for x in self) + ']'

    def __repr__(self):
        """Supports REPL inspection. (Same behavior as `str`.)"""
        return '[' + ', '.join(str(x) for x in self) + ']'

    ### single-element manipulation ###

    def insert(self, idx, value):
        """Inserts value at position idx, shifting the original elements down the
        list, as needed. Note that inserting a value at len(self) --- equivalent
        to appending the value --- is permitted. Raises IndexError if idx is invalid."""

    def pop(self, idx=-1):
        """Deletes and returns the element at idx (which is the last element,
        by default)."""

    def remove(self, value):
        """Removes the first (closest to the front) instance of value from the
        list. Raises a ValueError if value is not found in the list."""

    ### predicates (T/F queries) ###

    def __eq__(self, other):
        """Returns True if this LinkedList contains the same elements (in order) as
        other. If other is not an LinkedList, returns False."""
        if other is not LinkedList:  # check same time
            return False
        elif self.length != other.length:  # check same length
            return False
        else:  # iterate through list
            for i in range(self.length):
                if self[i] != other[i]:
                    return False

            return True

    def __contains__(self, value):
        """Implements `val in self`. Returns true if value is found in this list."""
        for val in iter(self):  # iterate through list
            if val == value:
                return True

        return False

    ### queries ###

    def __len__(self):
        """Implements `len(self)`"""
        return self.length

    def min(self):
        """Returns the minimum value in this list."""
        # init min
        min_val = self.head.val

        # iterate through list
        for i in iter(self):
            if i < min_val:
                min_val = i

        return min_val

    def max(self):
        """Returns the maximum value in this list."""
        max_val = self.head.val

        # iterate through list
        for i in iter(self):
            if i < max_val:
                max_val = i

        return max_val

    def index(self, value, i=0, j=None):
        """Returns the index of the first instance of value encountered in
        this list between index i (inclusive) and j (exclusive). If j is not
        specified, search through the end of the list for value. If value
        is not in the list, raise a ValueError."""
        # check for j
        if j is None:
            j = self.length

        # iterate through list
        for idx in range(i, j):
            if self[idx] == value:
                return idx

        # value not found, raise error
        raise ValueError

    def count(self, value):
        """Returns the number of times value appears in this list."""
        # init count
        count = 0

        # iterate through list
        for val in iter(self):
            if val == value:
                count += 1

        return count

    ### bulk operations ###

    def __add__(self, other):
        """Implements `self + other_list`. Returns a new LinkedList
        instance that contains the values in this list followed by those
        of other."""
        assert (isinstance(other, LinkedList))

        # init new list
        new_list = self.copy()

        # iterate through other, append values
        for val in iter(other):
            new_list.append(val)

        return new_list

    def clear(self):
        """Removes all elements from this list."""
        self.head.next = self.head.prior = self.head
        self.length = 0

    def copy(self):
        """Returns a new LinkedList instance (with separate Nodes), that
        contains the same values as this list."""
        # init new list
        new_list = LinkedList()

        # iterate through current list
        for val in iter(self):
            new_list.append(val)

        return new_list

    def extend(self, other):
        """Adds all elements, in order, from other --- an Iterable --- to this list."""
        for val in iter(other):
            self.append(val)

    ### iteration ###

    def __iter__(self):
        """Supports iteration (via `iter(self)`)"""
        if self.length == 0:
            return

        # get node for iteration
        node = self.head.next

        # iterate through nodes
        while node:
            yield node.val
            if node.next == self.head:
                return
            else:
                node = node.next
