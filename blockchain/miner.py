import hashlib
import requests

import sys

from uuid import uuid4

from timeit import default_timer as timer

import random


def proof_of_work(last_proof):
    """
    Multi-Ouroboros of Work Algorithm
    - Find a number p' such that the last six digits of hash(p) are equal
    to the first six digits of hash(p')
    - IE:  last_hash: ...AE9123456, new hash 123456888...
    - p is the previous proof, and p' is the new proof
    - Use the same method to generate SHA-256 hashes as the examples in class
    - Note:  We are adding the hash of the last proof to a number/nonce for the new proof
    """

    start = timer()

    print("Searching for next proof")
    proof = 0
    #  TODO: Your code here
    # here we just recieve the proof of work and we run with it since we validated it
    # and until the valid proof is back to TRUE it just keeps running and adding a proof
    while valid_proof(last_proof, proof) is False:
        proof += random.randint(1,101)

    print("Proof found: " + str(proof) + " in " + str(timer() - start))
    return proof


def valid_proof(last_hash, proof):
    """
    Validates the Proof:  Multi-ouroborus:  Do the last six characters of
    the hash of the last proof match the first six characters of the proof?

    IE:  last_hash: ...AE9123456, new hash 123456888...
    """

    # TODO: Your code here!
    # so we first recieve the proof to validate by a matching hash, it exitsts, or key
    # then we have to encode it so it can be converted to a hexidecimal

    guess_proof = f"{last_hash}{proof}".encode()

    # then we have to check it's history or hashses we convert the inport "last_hash" into a string
    last_hash = str(last_hash)

    # still don't know what this whole line does i just copied from my hw I think it rehashes the proof and "checks it history" by compairing it's hash with the pervious hash i'm still not too sure and the convert it into a hexideciemal
    hashed_proof = hashlib.sha256(guess_proof).hexdigest()

    # then we return the valid proof with the number of hashse are equal to the proof which returns a TRUE or FALSE and in this case SHOULD be FALSE
    return hashed_proof[:6] == last_hash[-6:]
    # pass


if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "https://lambda-coin.herokuapp.com/api"

    coins_mined = 0

    # Load or create ID
    f = open("my_id.txt", "r")
    id = f.read()
    print("ID is", id)
    f.close()

    if id == 'danHEElim\n':
        print("ERROR: You must change your name in `my_id.txt`!")
        exit()
    # Run forever until interrupted
    while True:
        # Get the last proof from the server
        r = requests.get(url=node + "/last_proof")
        data = r.json()
        new_proof = proof_of_work(data.get('proof'))

        post_data = {"proof": new_proof,
                     "id": id}

        r = requests.post(url=node + "/mine", json=post_data)
        data = r.json()
        if data.get('message') == 'New Block Forged':
            coins_mined += 1
            print("Total coins mined: " + str(coins_mined))
        else:
            print(data.get('message'))
