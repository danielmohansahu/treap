#!/usr/bin/env python
""" Run full suite of assignments for ENPM809X Project.
""" 
import os
import random
import timeit
import string
from pkg_resources import resource_filename

from pytreap.treap import Treap

# handy global variables
TIMED_COUNT=20

def is_ordered(treap):
    """ Utility to check that every node in the given Treap satisfies the following:
    Rules:
     - if v is a child of u, then v.priority <= u.priority
     - if v is a left child of u, then v.key < u.key
     - if v is a right child of u, then v.key > u.key
    """
    # iterate through all nodes in the heap
    for node in treap:
        # check parent (if not root)
        if node != treap.root and (node.priority > node.parent.priority):
            print("Node {} and parent ({}) have mismatched priorities.".format(node, node.parent))
            return False
        # check left and right. All are optional, technically
        if node.left and (node.key < node.left.key):
            print("Node {} and left child ({}) have mismatched keys.".format(node, node.left))
            return False
        if node.right and (node.key > node.right.key):
            print("Node {} and right child ({}) have mismatched keys.".format(node, node.right))
            return False
    return True

def read_and_search(treap, data):
    """ Search for each character in the given file (non-case-sensitive) in the given Treap.

    Repeats this operation TIMED_COUNT times and prints out the average time.

    Raises:
        AssertionError: If a character (A-Z) is not found.
    """
    # define core search method
    def _search():
        for c in data:
            if not(treap.search(c)):
                raise RuntimeError("Treap couldn't find expected key: '{}'.".format(c))

    print("Treap took {:.3f} seconds (average of {} tests) to search for {} characters.\n".format(
        timeit.timeit(_search, number=TIMED_COUNT)/TIMED_COUNT,
        TIMED_COUNT,
        len(data)))

def main():
    # seed random priorities
    random.seed()

    # find test data
    test_file = os.path.abspath(resource_filename('pytreap.data', 'textbook.txt'))
    test_data = open(test_file).read()
    if not len(test_data) == 164030:
        raise RuntimeError("Test data has unexpected length; something is wrong.")

    # (filesystem IO isn't part of the test!) pre-parse
    #  - strip out characters not in (A-Z,a-z)
    #  - convert (a-z) to uppercase
    test_data_cleaned = [c.upper() for c in test_data if c in string.ascii_letters]

    # define keys here, for convenience
    keys = ('Z','Y','X','W','V','Q','U','P','S','R','K','J','G','B',
            'F','C','M','D','H','I','L','A','N','O','T','E')
    ###############################################################################################
    ##################################### Part #3 #################################################
    ###############################################################################################
    statement = """
    Use TreapInsert to build a treap using uppercase letters as keys, received in the
    following order:

    {'Z','Y','X','W','V','Q','U','P','S','R','K','J','G','B',
    'F','C','M','D','H','I','L','A','N','O','T','E'}
    
    Use randomly generated treap priorities for each letter.

    Verify that your treap indeed satisfies the binary search tree and heap priorities.
    """
    print("Step #3 Problem Statement: \n{}".format(statement))

    # construct the desired treap (priorities are generated randomly implicitly)
    uniform_treap = Treap()

    # add all the keys
    for key in keys:
        uniform_treap.insert(key)

    # print out the resulting treap
    uniform_treap.display()

    # check that this satisfies our conditions
    if is_ordered(uniform_treap):
        print("\nSUCCESS: Resulting treap satisfies our conditions.\n")
    else:
        print("\nERROR: Resulting treap is not ordered properly. Something went wrong.\n")
    
    ###############################################################################################
    ##################################### Part #4 #################################################
    ###############################################################################################
    statement="""
    Write a program that will read the file “textbook.txt” character by character, which
    contains the preface of your textbook repeated several times. For each uppercase
    character (“A-Z”) that is read, use TreapSearch function to search your treap for that
    character (which should always find a match). For each lowercase character (“a-z”) that
    is read, convert it to uppercase and then use TreapSearch function to search your
    treap (again, it should always find a match). Skip all other characters that are read.
    Measure the total time it takes for searching all letters in the file.
    
    Run your program 5 times to get 5 measurement values, and then calculate the average
    of your measurements.
    """
    print("Step #4 Problem Statement: \n{}".format(statement))

    # test our speed against the Treap created in step #3
    read_and_search(uniform_treap, test_data_cleaned)

    ###############################################################################################
    ##################################### Part #5 #################################################
    ###############################################################################################
    statement="""
    Repeat steps 3 and 4 above, using the following priorities when generating the treap,
    instead of random priorities. These priorities roughly correspond to average frequency
    of each letter in English. When generating the treap, the characters should still be
    received in the order specified in step 3.

    Characters: A,B, C, D, E, F,G, H, I, J,K, L, M, N, O, P,Q, R, S, T, U,V,W,X,Y,Z
    Priorities: 24,7,14,17,26,10,8,18,22,4,5,16,13,19,23,12,2,20,21,25,15,6,11,3,9,1

    Run your program 5 times and calculate the average of your time measurements as in
    step 4. Does using priorities corresponding to letter frequency improve the running
    time?
    """
    print("Step #5 Problem Statement: \n{}".format(statement))

    # construct and add keys and priorities to this new Treap
    heuristic_keys = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    priorities = (24,7,14,17,26,10,8,18,22,4,5,16,13,19,23,12,2,20,21,25,15,6,11,3,9,1)
    heuristic_key_map = {k:p for k,p in zip(heuristic_keys, priorities)}

    # construct a heuristic Treap, still inserting keys in the order from the previous problem
    heuristic_treap = Treap()
    for k in keys:
        heuristic_treap.insert(k,heuristic_key_map[k])

    # print out the resulting treap
    print("Heuristic Treap:")
    heuristic_treap.display()

    # time the resulting search with test data
    read_and_search(heuristic_treap, test_data_cleaned)

    ###############################################################################################
    ##################################### Part #6 #################################################
    ###############################################################################################
    statement="""
    Repeat steps 3 and 4 above, without using any priorities when generating the treap,
    thus generating a simple binary search tree. Depending on your implementation, one
    way to do this may be assigning the same priority to all characters when calling the
    TreapInsert function. When generating the tree, the characters should still be
    received in the order specified in step 3.

    Run your program 5 times and calculate the average of your time measurements as in
    steps 4 and 5. Does using treaps improve the running time compared to a binary search
    tree?
    """
    print("Step #6 Problem Statement: \n{}".format(statement))

    # construct and add keys to this new Treap
    binary_treap = Treap()
    for key in keys:
        binary_treap.insert(key, 1)

    # print out the resulting treap
    print("Binary Tree Treap:")
    binary_treap.display()

    # time the resulting search with test data
    read_and_search(binary_treap, test_data_cleaned)

if __name__ == "__main__":
    main()
