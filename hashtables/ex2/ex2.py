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
        # here we are inserting a hash per the length of the tickets so here for example we have 5 tickets and so we insert the length of the ticket list, source ,and destination

        # we are starting the sequence so to speak so we can work with changing it around. 
       hash_table_insert(hashtable, ticket.source, ticket.destination)

    # here if find the location of the first airport which had no previous airport to fly from which will be our head so in the test case it will be ticket 1 PDX or in test2 LAX
    # so now we have our starting point and it's as simple as linking everything together since every ticket has a final destination
    location = hash_table_retrieve(hashtable, "NONE")

    # so we want to loop as long as the length of the list of tickets.
    for i in range(length):
        # the list above labled "route" has a list of a bunch of NONE's so we change FIRST index with the current location which is our head
        route[i] = location
        # then we retrieve the next location by running "hash_table_retrieve" with the hashtable and the current "location" as the previous airport it arrived from and replacing the current location vairable with the new found destination
        location = hash_table_retrieve(hashtable, location)

    # here we print because the READ ME said to
    print(route)
    # and now we return it
    return route
