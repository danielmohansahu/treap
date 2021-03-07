""" Treap Class Implementation

This class defines an Object Oriented Treap: a combination of a 
Binary Search Tree and a Heap.
"""

import random
from typing import Union

from .node import Node

class Treap:
    """ This class maintains a prioritized set of Nodes for efficient insertion
    and search operations.
    """

    def __init__(self) -> None:
        # default instantiation creates an empty treap
        self._nodes = []
        self._used_keys = set()

    def insert(self, key: str, priority: Union[int, None] = None) -> None:
        """ Insert a new key (and optionally a priority).

        Args:
            key: The string key of the new node.
            priority: An optional integer value; if None this is randomly generated.
        """
        # make sure this key hasn't been used previously
        if key in self._used_keys:
            raise AssertionError("Key {} already in use.".format(key))

        # make sure the given priority is good or generate our own    
        if priority is not None and priority < 0:
            raise AssertionError("Priority must be greater than zero.")
        else:
            priority = random.randint(0, 1000)
   
        # @TODO actually insert; for now just constructing / appending
        node = Node(key, priority)

        self._used_keys.add(key)
        self._nodes.append(node)

    def search(self, key: str) -> bool:
        """ Search for the given key in the treap and return True if found.

        Args:
            key: The string key to search for.

        Returns:
            Boolean indicating success or failure.
        """
        return False

    def __len__(self) -> int:
        # return the current size of the treap
        return len(self._nodes)

    def __iter__(self):
        return iter(self._nodes)

