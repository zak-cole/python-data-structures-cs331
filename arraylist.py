from constrainedlist import ConstrainedList

'''ArrayList Data Structure Implementation
    Illinois Tech CS331
'''


class ArrayList:
    def __init__(self):
        self.data = ConstrainedList()  # don't change this line!

    ### subscript-based access ###

    def _normalize_idx(self, idx):
        nidx = idx
        if nidx < 0:
            nidx += len(self.data)
            if nidx < 0:
                nidx = 0
        return nidx

    def __getitem__(self, idx):
        """Implements `x = self[idx]`"""
        assert (isinstance(idx, int))
        nidx = self._normalize_idx(idx)
        if nidx >= len(self.data):
            raise IndexError
        return self.data[nidx]

    def __setitem__(self, idx, value):
        """Implements `self[idx] = x`"""
        assert (isinstance(idx, int))
        nidx = self._normalize_idx(idx)
        if nidx >= len(self.data):
            raise IndexError
        self.data[nidx] = value

    def __delitem__(self, idx):
        """Implements `del self[idx]`"""
        assert (isinstance(idx, int))
        nidx = self._normalize_idx(idx)
        if nidx >= len(self.data):
            raise IndexError
        for i in range(nidx + 1, len(self.data)):
            self.data[i - 1] = self.data[i]
        del self.data[len(self.data) - 1]

    ### stringification ###

    # todo implement
    def __str__(self):
        """Implements `str(self)`. Returns '[]' if the list is empty, else
        returns `str(x)` for all values `x` in this list, separated by commas
        and enclosed by square brackets. E.g., for a list containing values
        1, 2 and 3, returns '[1, 2, 3]'."""

        # list is empty
        if len(self) == 0:
            return '[]'

        # list is not empty
        iterator = iter(self)
        str_rep = '['
        count = 0

        # iterator loop
        while True:
            try:
                # append next item to string
                str_rep += str(next(iterator))

                # fence post case
                if count < len(self) - 1:
                    str_rep += ', '

                count += 1
            except StopIteration:
                str_rep += ']'
                break

        return str_rep

    def __repr__(self):
        """Supports REPL inspection. (Same behavior as `str`.)"""
        # list is empty
        if len(self) == 0:
            return '[]'

        # list is not empty
        iterator = iter(self)
        str_rep = '['
        count = 0

        # iterator loop
        while True:
            try:
                # append next item to string
                str_rep += str(next(iterator))

                # fence post case
                if count < len(self) - 1:
                    str_rep += ', '

                count += 1
            except StopIteration:
                str_rep += ']'
                break

        return str_rep

    ### single-element manipulation ###

    def append(self, value):
        """Appends value to the end of this list."""
        self.data.append(None)
        self.data[len(self.data) - 1] = value

    # todo implement
    def insert(self, idx, value):
        """Inserts value at position idx, shifting the original elements down the
        list, as needed. Note that inserting a value at len(self) --- equivalent
        to appending the value --- is permitted. Raises IndexError if idx is invalid."""

    def pop(self, idx=-1):
        """Deletes and returns the element at idx (which is the last element,
        by default)."""

        # get and delete item
        item = self[idx]
        del self[idx]

        return item

    def remove(self, value):
        """Removes the first (closest to the front) instance of value from the
        list. Raises a ValueError if value is not found in the list."""

        # get index
        idx = self.index(value)

        # remove item
        del self[idx]

    ### predicates (T/F queries) ###

    def __eq__(self, other):
        """Returns True if this ArrayList contains the same elements (in order) as
        other. If other is not an ArrayList, returns False."""

        # check if other is an ArrayList
        if other is ArrayList:
            # iterate through values in list
            for idx in range(len(self.data)):
                # items are not equal
                if self.data[idx] != other[idx]:
                    return False

            # all items are equal, return true
            return True
        else:
            # other is not an ArrayList, return false
            return False

    def __contains__(self, value):
        """Implements `val in self`. Returns true if value is found in this list."""

        # iterate through data
        iterator = iter(self)
        while True:
            try:
                if next(iterator) == value:
                    return True
            except StopIteration:
                break

        # data not found, return false
        return False

    ### queries ###

    def __len__(self):
        """Implements `len(self)`"""
        return len(self.data)

    def min(self):
        """Returns the minimum value in this list."""

        # init min
        minimum = self.data[0]

        # iterate through data
        iterator = iter(self)
        while True:
            try:
                item = next(iterator)
                if item < minimum:
                    minimum = item
            except StopIteration:
                break

        # return minimum value
        return minimum

    def max(self):
        """Returns the maximum value in this list."""

        # init max
        maximum = self.data[0]

        # iterate through data
        iterator = iter(self)
        while True:
            try:
                item = next(iterator)
                if item > maximum:
                    maximum = item
            except StopIteration:
                break

        # return maximum value
        return maximum

    def index(self, value, i=0, j=None):
        """Returns the index of the first instance of value encountered in
        this list between index i (inclusive) and j (exclusive). If j is not
        specified, search through the end of the list for value. If value
        is not in the list, raise a ValueError."""

        # check if j is none
        if j is None:
            j = len(self)

        # iterate through list
        for idx in range(i, j):
            if self.data[idx] == value:
                return idx

        # data not found, raise value error
        raise ValueError()

    def count(self, value):
        """Returns the number of times value appears in this list."""

        # init count
        count = 0

        # iterate through data
        iterator = iter(self)
        while True:
            try:
                item = next(iterator)
                if item == value:
                    count += 1
            except StopIteration:
                break

        return count

    ### bulk operations ###

    def __add__(self, other):
        """Implements `self + other_array_list`. Returns a new ArrayList
        instance that contains the values in this list followed by those
        of other."""

        # check that other is arraylist
        if other is ArrayList:
            # init new list
            new_list = ArrayList()

            # add items in self to new list
            iterator = iter(self)
            while True:
                try:
                    new_list.append(next(iterator))
                except StopIteration:
                    break

            # add items in other list to new list
            iterator = iter(other)
            while True:
                try:
                    new_list.append(next(iterator))
                except StopIteration:
                    break

            return new_list

    def clear(self):
        self.data = ConstrainedList()  # don't change this!

    def copy(self):
        """Returns a new ArrayList instance (with a separate data store), that
        contains the same values as this list."""

        # init new list
        new_list = ArrayList()

        # add items in current list to new list
        iterator = iter(self)
        while True:
            try:
                new_list.append(next(iterator))
            except StopIteration:
                break

        return new_list

    def extend(self, other):
        """Adds all elements, in order, from other --- an Iterable --- to this list."""

    ### iteration ###

    def __iter__(self):
        """Supports iteration (via `iter(self)`)"""
        for i in range(len(self.data)):
            yield self.data[i]
