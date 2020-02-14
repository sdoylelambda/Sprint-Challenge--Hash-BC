#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)




def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    print('ht:', ht) # obj
    print('weights:', weights) # []
    print('length:', length) # int
    print('limit:', limit) # int

    """
    # store each weight in the input list as keys
    # Store each weight's list index as its value, 
    # we can then check to see if the hash table contains
    # an entry for `limit - weight`. 
    # If it does, then we've found the two items whose weights sum up to the `limit`!

    """
# while?
    for weight in weights:
        # store each weight in the input list as keys -- []
        # Store each weight's list index as its value, --
        hash_table_insert(ht, weight, length)
        # print('ht2:', ht)
        print('weight:', weight)
        # we can then check to see if the hash table contains
        x = hash_table_retrieve(ht, weight)
        # an entry for `limit - weight`.
        # if hash_table.contains(f'{limit} - {weights}'):
        if limit - weight == limit:

        # If it does, then we've found the two items whose weights sum up to the `limit`!
            return limit, weight




def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

# TEST

 # def test_ex1_1(self):
 #        weights_1 = [9]
 #        answer_1 = get_indices_of_item_weights(weights_1, 1, 9)
 #        self.assertTrue(answer_1 is None)