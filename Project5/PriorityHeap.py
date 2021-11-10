from math import floor
from typing import List, Tuple, Any


class Node:
    """
    Node definition should not be changed in any way
    """
    __slots__ = ['key', 'value']

    def __init__(self, k: Any, v: Any):
        """
        Initializes node
        :param k: key to be stored in the node
        :param v: value to be stored in the node
        """
        self.key = k
        self.value = v

    def __lt__(self, other):
        """
        Less than comparator
        :param other: second node to be compared to
        :return: True if the node is less than other, False if otherwise
        """
        return self.key < other.key or (self.key == other.key and self.value < other.value)

    def __gt__(self, other):
        """
        Greater than comparator
        :param other: second node to be compared to
        :return: True if the node is greater than other, False if otherwise
        """
        return self.key > other.key or (self.key == other.key and self.value > other.value)

    def __eq__(self, other):
        """
        Equality comparator
        :param other: second node to be compared to
        :return: True if the nodes are equal, False if otherwise
        """
        return self.key == other.key and self.value == other.value

    def __str__(self):
        """
        Converts node to a string
        :return: string representation of node
        """
        return '({0}, {1})'.format(self.key, self.value)

    __repr__ = __str__


class PriorityQueue:
    """
    Partially completed data structure. Do not modify completed portions in any way
    """
    __slots__ = ['data']

    def __init__(self):
        """
        Initializes the priority heap
        """
        self.data = []

    def __str__(self) -> str:
        """
        Converts the priority heap to a string
        :return: string representation of the heap
        """
        return ', '.join(str(item) for item in self.data)

    __repr__ = __str__

    def to_tree_format_string(self) -> str:
        """
        Prints heap in Breadth First Ordering Format
        :return: String to print
        """
        string = ""
        # level spacing - init
        nodes_on_level = 0
        level_limit = 1
        spaces = 10 * int(1 + len(self))

        for i in range(len(self)):
            space = spaces // level_limit
            # determine spacing

            # add node to str and add spacing
            string += str(self.data[i]).center(space, ' ')

            # check if moving to next level
            nodes_on_level += 1
            if nodes_on_level == level_limit:
                string += '\n'
                level_limit *= 2
                nodes_on_level = 0
            i += 1

        return string

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   Modify below this line

    def __len__(self) -> int:
        """
        Retrieves length of the PriorityQueue
        :return: Integer length value.
        """
        return len(self.data)

    def empty(self) -> bool:
        """
        Determines if the PriorityQueue is empty.
        :return: True if PriorityQueue is empty, false otherwise.
        """
        return len(self.data) == 0

    def top(self) -> Node:
        """
        Retrieves the top node from the PriorityQueue.
        :return: Root Node.
        """
        if not self.empty():
            return self.data[0]
        else:
            return None

    def get_left_child_index(self, index: int) -> int:
        """
        Retrieves the index of the left child in relation to the passed index.
        :param index: Index of Node to retrieve left child from.
        :return: Integer index of left child.
        """
        left_index = (index * 2) + 1
        if left_index >= len(self.data):
            return None
        return (index * 2) + 1

    def get_right_child_index(self, index: int) -> int:
        """
        Retrieves the index of the right child in relation to the passed index.
        :param index: Index of Node to retrieve right child from.
        :return: Integer index of right child.
        """
        right_index = (index * 2) + 2
        if right_index >= len(self.data):
            return None
        return (index * 2) + 2

    def get_parent_index(self, index: int) -> int:
        """
        Retrieves the index of the right child in relation to the passed index.
        :param index: Index of Node to retrieve right child from.
        :return: Integer index of right child.
        """
        parent_index = floor((index - 1) / 2)
        if parent_index > len(self.data) or parent_index < 0:
            return None
        return floor((index - 1) / 2)

    def push(self, key: Any, val: Any) -> None:
        """
        Adds a node to the heap, with position in heap based on key parameter.
        :param key: Priority key.
        :param val: Value
        :return: None
        """
        self.data.append(Node(key, val))
        self.percolate_up(len(self) - 1)

    def pop(self) -> Node:
        """
        Removes the smallest element Node from the priority queue.
        :return: Node that was removed
        """
        if not self.empty():
            self.data[0], self.data[len(self) - 1] = self.data[len(self) - 1], self.data[0]
            returned_node = self.data.pop()
            self.percolate_down(0)
            return returned_node

    def get_min_child_index(self, index: int) -> int:
        """
        Retrieve the index of the smaller child of the passed parent index.
        :param index: Integer index of parent that children are examined on.
        :return: Integer value of index if minimum child exists, None otherwise.
        """
        left_child = self.get_left_child_index(index)
        right_child = self.get_right_child_index(index)
        if left_child is not None and right_child is not None:
            return left_child if self.data[left_child] < self.data[right_child] else right_child
        return left_child

    def percolate_up(self, index: int) -> None:
        """
        Moves a node to a valid spot in the heap.
        :param index: Index of node to move.
        :return: None
        """
        if not self.empty():
            parent_index = self.get_parent_index(index)
            while parent_index is not None and self.data[index] < self.data[parent_index]:
                # swap parent and child
                self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
                index = parent_index
                parent_index = self.get_parent_index(index)

    def percolate_down(self, index: int) -> None:
        """
        Move a node down to a valid spot in the heap.
        :param index: Index of node to move.
        :return: None
        """
        if not self.empty() and len(self) > 1:
            min_child = self.get_min_child_index(index)
            while min_child is not None and self.data[index] > self.data[min_child]:
                # swap parent with the minimum child
                self.data[min_child], self.data[index] = self.data[index], self.data[min_child]
                index = min_child
                min_child = self.get_min_child_index(index)


class MaxHeap:
    """
    Partially completed data structure. Do not modify completed portions in any way
    """
    __slots__ = ['data']

    def __init__(self):
        """
        Initializes the priority heap
        """
        self.data = PriorityQueue()

    def __str__(self):
        """
        Converts the priority heap to a string
        :return: string representation of the heap
        """
        return ', '.join(str(item) for item in self.data.data)

    def __len__(self):
        """
        Length override function
        :return: Length of the data inside the heap
        """
        return len(self.data)

    def print_tree_format(self):
        """
        Prints heap in bfs format
        """
        self.data.tree_format()

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   Modify below this line

    def empty(self) -> bool:
        """
        Determines if the MaxHeap is empty.
        :return: True if the MaxHeap is empty, false otherwise.
        """
        return self.data.empty()

    def top(self) -> int:
        """
        Finds the root value of the MaxHeap.
        :return: Root node of MaxHeap, None if root node does not exist.
        """
        if not self.empty():
            return -self.data.top().value
        else:
            return None

    def push(self, key: int) -> None:
        """
        Adds a value to the heap.
        :param key: Value of element to be added to heap.
        :return: None
        """
        self.data.push(-key, -key)

    def pop(self) -> int:
        """
        Removes the largest element from the Heap.
        :return: Largest element that was removed. If the heap was empty, returns None.
        """
        if self.data.empty():
            return None
        return -self.data.pop().value


def heap_sort(array):
    """
    Sorts the given list in-place in ascending order using a MaxHeap.
    :param array: List to be sorted.
    :return: Array list that is sorted.
    """
    my_heap = MaxHeap()
    for i in array:
        my_heap.push(i)
    index = len(array) - 1

    while not my_heap.empty():
        # remove the max value
        # store that value at the end index
        array[index] = my_heap.pop()
        # decrement the end index (shrink .len of array by 1?)
        index -= 1
        # repeat until end index is 0
    return array


def find_ranking(rank, results: List[Tuple[int, str]]) -> str:
    """
    Given a list of tuples containing the amount of losses and a team name,
    find the team that had the given rank.
    :param rank: Rank of team to find.
    :param results: List of Tuples containing [number of losses, team name]
    :return: Team with the passed rank.
    """
    if rank <= len(results):
        sorter = PriorityQueue()
        for losses, team_name in results:
            sorter.push(losses, team_name)
        for i in range(rank):
            removed = sorter.pop()
        return removed.value
