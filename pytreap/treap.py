""" Treap Class Implementation

This class defines an Object Oriented Treap: a combination of a 
Binary Search Tree and a Heap.
"""

from typing import Union

from .node import Node

class Treap:
    """ This class maintains a prioritized set of Nodes for efficient insertion
    and search operations.
    """

    def __init__(self) -> None:
        # default instantiation creates an empty treap
        pass

    def insert(self, key: str, priority: Union[int, None]) -> None:
        """ Insert a new key (and optionally a priority).

        Args:
            key: The string key of the new node.
            priority: An optional integer value; if None this is randomly generated.
        """
        pass

    def search(self, key: str) -> bool:
        """ Search for the given key in the treap and return True if found.

        Args:
            key: The string key to search for.

        Returns:
            Boolean indicating success or failure.
        """
        pass

    def __len__(self) -> bool:
        # return the current size of the treap
        pass


