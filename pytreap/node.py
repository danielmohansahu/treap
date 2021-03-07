""" Node Class used as the basic data structure of the Treap class.

@TODO:
 - Handle random assignment of priority
"""

from typing import Union

class Node:
    # member variables
    key: str
    priority: Union[int, None]
    parent: Union[Node, None]
    left: Union[Node, None]
    right: Union[Node, None]

    def __init__(self,
                 key: str,
                 priority: Union[int, None] = None) -> None:
        pass

