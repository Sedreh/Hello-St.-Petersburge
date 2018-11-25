__author__ = 'DELLIRAN'


class QueueNode(object):
    """Node: Class for single node of LinkedQueue."""

    def __init__(self, elem, nextnode):
        """Method. Initializes new node."""
        self.value = elem
        self.next = nextnode


class QueueIterator(object):
    """QueueIterator: Iterator for LinkedQueue."""

    def __init__(self, node, count):
        """Method. Initializes new Iterator."""
        self.end = node
        self.count = count

    def __next__(self):
        """Method. Returns next element of queue: next(iter)."""
        if self.count == 0:
            raise StopIteration
        else:
            end = self.end.value
            self.end = self.end.next
            self.count -= 1
            return end


class LinkedQueue(object):
    """LinkedQueue."""

    def __init__(self):
        """Method. Initializes new queue."""
        self.first = None
        self.end = None
        self.count = 0

    def push(self, elem):
        """Method. Pushes 'elem' to queue."""
        new_node = QueueNode(elem)
        if self.end is not None:
            # make the front attribute of old node point to new node
            self.end.front = new_node
        else:
            # if first ever node in Queue both front and tail will point to it
            self.first = new_node

        self.end = new_node
        self.count += 1


    def pop(self):
        """Method. Removes front of queue and returns it."""
        end = self.end.value
        self.end = self.end.next
        self.count -= 1
        return end

    def front(self):
        """Method. Returns front of queue."""
        return self.end.value

    def empty(self):
        """Method. Checks whether queue is empty."""
        return not self.count

    def __iter__(self):
        """Method. Returns Iterator for queue: iter(queue)."""
        return QueueIterator(self.end, self.count)

    def __len__(self):
        """Method. Returns size of queue: len(queue)."""
        return self.count

    def clear(self):
        """Method. Makes queue empty."""
        self.first = None
        self.end = None
        self.count = 0
