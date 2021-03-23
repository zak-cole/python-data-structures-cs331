class OrderedHashtable:
    class Node:
        """This class is used to create nodes in the singly linked "chains" in
        each hashtable bucket."""

        def __init__(self, index, next=None):
            # don't rename the following attributes!
            self.index = index
            self.next = next

    # initialize ordered hashtable
    def __init__(self, n_buckets=1000):
        # the following two variables should be used to implement the "two-tiered"
        # ordered hashtable described in class -- don't rename them!
        self.indices = [None] * n_buckets
        self.entries = []
        self.count = 0

    # get item from hashtable
    def __getitem__(self, key):
        # get index of bucket
        bucket_idx = hash(key) % len(self.indices)

        # get desired node
        node = self.indices[bucket_idx]

        # iterate through map
        while node is not None:
            if self.entries[node.index][0] == key:
                return self.entries[node.index][1]
            node = node.next

        # key not found
        raise KeyError

    # set item in hashtable
    def __setitem__(self, key, val):
        # get bucket index
        bucket_idx = hash(key) % len(self.indices)

        # get node
        node = self.indices[bucket_idx]

        # iterate
        value = len(self.entries)
        if node is None:
            self.entries.append([key, val])
            self.count += 1
            self.indices[bucket_idx] = OrderedHashtable.Node(value)
        else:
            node = self.indices[bucket_idx]
            while node is not None:
                temp = self.entries[node.index]
                if temp[0] == key:
                    temp[1] = val
                    return
                if node.next is None:
                    self.entries.append([key, val])
                    new_node = OrderedHashtable.Node(value)
                    node.next = new_node
                    self.count += 1
                    return
                node = node.next

    # remove item from ordered hashtable
    def __delitem__(self, key):
        # get item to delete
        bucket_idx = hash(key) % len(self.indices)
        node = self.indices[bucket_idx]
        temp = self.entries[node.index]
        del_index = None

        # delete logic
        if temp[0] == key:
            self.count -= 1
            del_index = node.index
            del self.entries[node.index]
            if node.next is None:
                self.indices[bucket_idx] = None
            else:
                self.indices[bucket_idx] = node.next
        else:
            while node:
                prev = node
                node = node.next
                if self.entries[node.index][0] == key:
                    self.count -= 1
                    del self.entries[node.index]
                    del_index = node.index
                    prev.next = node.next
                    break
            else:
                raise KeyError
        for bucket in self.indices:
            node = bucket
            while node is not None:
                if node.index > del_index:
                    node.index -= 1
                node = node.next

    # check to see if hashtable contains key
    def __contains__(self, key):
        try:
            _ = self[key]
            return True
        except:
            return False

    # get length of hashtable
    def __len__(self):
        return self.count

    # iterate through keys
    def __iter__(self):
        # iterate through buckets
        for i in self.entries:
            yield i[0]

    # iterate through keys
    def keys(self):
        return iter(self)

    # iterate through values
    def values(self):
        for i in self.entries:
            yield i[1]

    # iterate through key, value pairs
    def items(self):
        for i in self.entries:
            yield i[0], i[1]

    # return string of hashtable
    def __str__(self):
        return '{ ' + ', '.join(str(k) + ': ' + str(v) for k, v in self.items()) + ' }'

    # return representation of hashtable
    def __repr__(self):
        return str(self)
