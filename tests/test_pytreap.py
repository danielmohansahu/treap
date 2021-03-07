""" Unit Tests for the pytreap.Treap class.
"""

import unittest
from typing import Tuple
import random
import string

from pytreap.treap import Treap

class TestTreap(unittest.TestCase):

    def test_construction(self):
        # basic sanity check of construction of a new Treap
        treap = Treap()

        # test length magic method
        self.assertEqual(len(treap), 0)

        # test iteration
        for node in treap:
            self.fail("Iteration over Treap failed; not empty as expected.")

    def test_insert(self):
        # test insertion with a known data set

        # first, construct an empty Treap
        treap = Treap()

        # insert a handful of known Nodes
        treap.insert("a", 1)
        treap.insert("b", 2)
        treap.insert("c", 3)
        treap.insert("d", 4)
        treap.insert("e", 5)

        # make sure there are 5 elements in the treap now
        self.assertEqual(len(treap), 5)

        # check that everything got constructed properly
        self.is_ordered(treap)

    def test_bad_insert(self):
        # evaluate insertion of improper values

        # first, construct an empty Treap
        treap = Treap()

        # try to insert a negative value (should fail)
        with self.assertRaises(AssertionError, msg="Allowed insertion of a negative priority"):
            treap.insert("a", -1)

    def test_random_insert(self):
        # make sure the public API method 'insert' behaves as expected
        #  for a variety of randomized inputs

        # all the checks are embedded in this method
        treap, keys = self.get_random_treap()

    def test_search(self):
        # test search with a known data set

        # first, construct an empty Treap
        treap = Treap()

        # make sure any search fails here
        self.assertFalse(treap.search("a"))
        self.assertFalse(treap.search("b"))
        self.assertFalse(treap.search("Napolean"))

        # insert a key and make sure we find it
        treap.insert("a")
        self.assertTrue(treap.search("a"))
        self.assertFalse(treap.search("b"))

        # insert a bunch more and make sure they all can be found
        for char in ("b", "c", "d", "e"):
            treap.insert(char)
            self.assertTrue(treap.search(char))

    def test_random_search(self):
        # make sure the public API method 'search' behaves as expected
        #  for a variety of randomized inputs

        # create a randomly populated ordered treap
        treap, keys = self.get_random_treap()

        # make sure we can find all the keys in the treap
        for key in keys:
            self.assertTrue(treap.find(key))

    def is_ordered(self, treap: Treap) -> None:
        """ Utility to check that every node in the given Treap satisfies the following:
        
        Rules:
         - if v is a child of u, then v.priority <= u.priority
         - if v is a left child of u, then v.key < u.key
         - if v is a right child of u, then v.key > u.key
        """
    
        # iterate through all nodes in the heap
        for node in treap:
            # check all three of parent, left, and right. All are optional, technically
    
            if node.parent:
                self.assertLessEqual(node.priority, node.parent.priority)
            if node.left:
                self.assertGreater(node.key, node.left.key)
            if node.right:
                self.asserLess(node.key, node.right.key)

    def get_random_treap(self) -> Tuple[Treap, set]:
        """ Utility method to randomly generate a Treap"
        """
        # first, construct an empty Treap
        treap = Treap()

        # initialize variables (number of entries + bookkeeping lists)
        used_keys = set()
        count = random.randint(100, 200)

        # randomly insert a lot of values
        for c in range(count):
            # generate random key (not necessarily unique!)
            key = random.choice(string.ascii_letters)

            # if key is already used, make sure this causes a failure condition
            if key in used_keys:
                with self.assertRaises(AssertionError, msg="Failed to raise an error with duplicate key insertion."):
                    treap.insert(key) 
            else:
                # add it to the list and insert this new value
                used_keys = used_keys.union(key)

                # either use a manually specified priority or an internally generated one 
                treap.insert(key, random.randint(0, count) if random.random() > 0.5 else None)

        # sanity check constructed treap
        self.assertEqual(len(treap), len(used_keys))
        self.is_ordered(treap)

        # return the generated structure
        return (treap, used_keys)

