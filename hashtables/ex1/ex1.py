#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    Merging Two Packages
Given a package with a weight limit limit and a list weights of item weights, implement a function 
get_indices_of_item_weights that finds two items whose sum of weights equals the weight limit limit. 
Your function will return an instance of an Answer tuple that has the following form:

(zero, one)
where each element represents the item weights of the two packages. The higher valued index should be placed in the 
zeroth index and the smaller index should be placed in the first index. If such a pair doesn’t exist for the given 
inputs, your function should return None.

NOTE: When calling hash_table_retrieve with a key that doesn't exist in the hash table, hash_table_retrieve will 
return None.

Your solution should run in linear time.

Example:

input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21
Hints

What if we store each weight in the input list as keys? 

What would be a useful thing to store as the value for each key?

If we store each weight's list index as its value, we can then check to see if the hash table contains an 
entry for limit - weight. If it does, then we've found the two items whose weights sum up to the limit!
    
    YOUR CODE HERE
    """

# store each weight in the input list as keys
    for i in range(0, len(weights)):
        wt = weights[i]
        print('wt:', wt)

        retrieve = hash_table_retrieve(ht, limit-wt)
        print('retrieve:', retrieve)
        if retrieve is not None:
            first = max(i, retrieve)
            print('first:', first)
            second = min(i, retrieve)
            print('second:', second)
            return (first, second)

        hash_table_insert(ht, wt, i)
        # breakpoint()
        print('ht:', ht)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
