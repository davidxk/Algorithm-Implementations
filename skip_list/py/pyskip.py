import random


__author__ = 'Daniel Lindsley'
__license__ = 'BSD'
__version__ = (0, 9, 0)


class InsertError(Exception):
    pass


class SingleNode(object):
    """
    A simple, singly linked list node.
    """
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return "{0}: {1}".format(self.__class__.__name__, self.value)

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ne__(self, other):
        return self.value != other.value


class LinkedList(object):
    """
    A simple linked list.
    """
    def __init__(self):
        self.head = None

    def __str__(self):
        return 'LinkedList: {0} items starting with {1}'.format(
            len(self),
            self.head.value
        )

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration()

        cur = self.current
        self.current = cur.next
        return cur
    # For Python 2.X-compat.
    next = __next__

    def __len__(self):
        count = 0

        for node in self:
            count += 1

        return count

    def __getitem__(self, offset):
        if offset < 0:
            raise IndexError(
                "Can't do negative offsets with a singly linked list."
            )

        for i, node in enumerate(self):
            if offset == i:
                return node

        raise IndexError("Index '{0}' out of range.".format(offset))

    def __contains__(self, value):
        return self.find(value) is not None

    def find(self, value):
        for node in self:
            if node.value == value:
                # We found it! Yay! Bail early.
                return node

        return None

    def insert_first(self, insert_node):
        """
        Inserts the new node at the beginning of the list.
        """
        insert_node.next = self.head
        self.head = insert_node
        return insert_node

    def insert_after(self, existing_node, insert_node):
        """
        Inserts the new node after a given node in the list.
        """
        insert_node.next = existing_node.next
        existing_node.next = insert_node
        return insert_node

    def remove_first(self):
        """
        Removes the first node (if any) in the list.
        """
        if self.head is None:
            return None

        old_head = self.head
        self.head = self.head.next
        return old_head

    def remove_after(self, existing_node):
        """
        Removes the node (if any) that follows the provided node in the list.
        """
        if existing_node.next is None:
            return None

        old_next = existing_node.next
        existing_node.next = existing_node.next.next
        return old_next


class SortedLinkedList(LinkedList):
    """
    A linked list that maintains the correct sort order.
    """
    def find(self, value):
        # We can be more efficient here, since we know we're sorted.
        for node in self:
            if node.value == value:
                # We found it! Yay! Bail early.
                return node

            if node.value > value:
                # We've exceeded the value & we didn't already come across it.
                # Must not be here. Bail.
                return None

        return None

    def insert_after(self, existing_node, new_node):
        if not existing_node <= new_node:
            raise InsertError("Invalid placement for the new node.")

        if existing_node.next and not new_node <= existing_node.next:
            raise InsertError("Invalid placement for the new node.")

        return super(SortedLinkedList, self).insert_after(
            existing_node,
            new_node
        )

    def insert_first(self, new_node):
        if self.head and not new_node <= self.head:
            raise InsertError("Invalid placement for the new node.")

        return super(SortedLinkedList, self).insert_first(new_node)

    def insert(self, new_node):
        if not self.head or new_node < self.head:
            self.insert_first(new_node)
            return

        previous = self.head

        for node in self:
            if previous <= new_node <= node:
                self.insert_after(previous, new_node)
                return

            previous = node

        return self.insert_after(previous, new_node)

    def remove(self, remove_node):
        previous = self.head

        for node in self:
            if node == remove_node:
                return self.remove_after(previous)

            previous = node

        return None


class SkiplistNode(SingleNode):
    def __init__(self, value=None, next=None, down=None):
        super(SkiplistNode, self).__init__(value=value, next=next)
        self.down = down


class SkipList(object):
    """
    Implements a basic skiplist.

    A skiplist provides a quickly searchable structure (like a balanced binary
    tree) that also updates fairly cheaply (no nasty rebalancing acts).

    In other words, it's awesome.

    See http://en.wikipedia.org/wiki/Skip_list for more information.
    """
    list_class = SortedLinkedList
    node_class = SkiplistNode
    max_layers = 32

    def __init__(self, list_class=None, node_class=None, max_layers=None):
        if list_class is not None:
            self.list_class = list_class

        if node_class is not None:
            self.node_class = node_class

        if max_layers is not None:
            self.max_layers = max_layers

        self.layers = [
            self.list_class()
        ]

    def __str__(self):
        return 'Skiplist: {0} items'.format(len(self.layers[-1]))

    def __len__(self):
        return len(self.layers[-1])

    def __contains__(self, value):
        return self.find(value) is not None

    def __iter__(self):
        return iter(self.layers[-1])

    def generate_height(self):
        """
        Generates a random height (between ``2`` & ``self.max_layers``) to fill
        in.
        """
        return random.randint(2, self.max_layers)

    def find(self, value):
        """
        Looks for a given value within the skiplist.

        Returns the node if found, ``None`` if the value was not found.
        """
        layer_offset = 0
        current = self.layers[layer_offset].head
        is_first = True

        while True:
            if current is None:
                # We've exhausted all options. Bail out.
                break

            if current.value == value:
                # We found it! Bail out.
                return current
            elif current.value > value:
                if is_first:
                    # We're at the beginning of the list, but there may be
                    # levels below with numbers befor this one.
                    layer_offset += 1

                    if layer_offset <= len(self.layers) - 1:
                        current = self.layers[layer_offset].head
                        continue
                    else:
                        break

            if current.next and current.next.value <= value:
                # The next node in the current layer might match.
                current = current.next
                is_first = False
                continue
            else:
                # Either the next node is too high or we reached the end of that
                # layer. Attempt to descend.
                if current.down is not None:
                    current = current.down
                    layer_offset += 1
                    continue
                else:
                    break

        return None

    def add(self, value, **kwargs):
        num_layers = len(self.layers)
        height = self.generate_height()

        # Make sure we have enough layers to accommodate.
        if height > num_layers:
            for i in range(num_layers, height):
                self.layers.insert(0, self.list_class())

        down = None

        for i in range(height):
            new_node = self.node_class(value=value, **kwargs)
            self.layers[num_layers - (i + 1)].insert(new_node)
            new_node.down = down
            down = new_node

    def remove(self, value):
        node = self.find(value)

        if node is None:
            return None

        # FIXME: This is bad.
        #        The other operations can be O(log N), but without knowing what
        #        layer offset we found the node in, we can't properly remove it
        #        without reaching in.
        #        For now, let's settle on something that works but is slow.
        for layer in self.layers:
            layer.remove(node)

    def debug(self, column_width=4):
        """
        Prints a representation of the skiplist's structure.

        Default ``column_width`` parameter is ``4``.
        """
        column_format_string = "{:" + str(column_width) + "} "
        full = self.layers[-1]

        for layer_offset, layer in enumerate(self.layers):
            print "{:<3}".format(layer_offset)

            for node in full:
                if node.value in layer:
                    print column_format_string.format(node.value)
                else:
                    print "     "

            print 
