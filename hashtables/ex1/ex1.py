#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    # print(ht)
    for index, item in enumerate(weights):
        match = hash_table_retrieve(ht, limit-item)
        if match is not None:
            if index > match:
                return(index, match)
            return (match, index)
        else:
            hash_table_insert(ht, item, index)


    """
    YOUR CODE HERE
    """


    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
