import hashlib
import json
import time


class Blockchain:

    def __init__(self):
        self.chain = []
        self.transactions = []

        # vytvoreni prvniho bloku
        self.create_block("0")

    def create_block(self, previous_hash):

        block = {
            "index": len(self.chain) + 1,
            "time": str(time.time()),
            "transactions": self.transactions,
            "previous_hash": previous_hash
        }

        self.transactions = []
        self.chain.append(block)

        return block

    def add_transaction(self, sender, receiver, amount):

        transaction = {
            "sender": sender,
            "receiver": receiver,
            "amount": amount
        }

        self.transactions.append(transaction)

    def hash(self, block):

        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def last_block(self):

        return self.chain[-1]
