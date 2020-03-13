#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length - 1)

    """
    YOUR CODE HERE
    """

    for t in tickets:
        print(t.source)
        print(t.destination)
        hash_table_insert(hashtable, t.source, t.destination)

    route[0] = hash_table_retrieve(hashtable, "NONE")
    for i in range(1, length - 1):
        route[i] = hash_table_retrieve(hashtable, route[i-1])

    return route

    return route