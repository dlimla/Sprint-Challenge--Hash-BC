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
    hashtable = HashTable(length) # 5
    route = [None] * length #[None,None,None,None,None,]

    """
    YOUR CODE HERE
    """

    for ticket in tickets:
        # here we are inserting a hash per the length of the tickets so here forexample we have 5 tickets and so we insert the length of the ticket list, source ,and destination
       hash_table_insert(hashtable, ticket.source, ticket.destination)

    # here if find the location of 
    location = hash_table_retrieve(hashtable, "NONE")

    for i in range(length):
        route[i] = location
        location = hash_table_retrieve(hashtable, location)

    print(route)

    return route
