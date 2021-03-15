import datetime
import hashlib
import json
import random

class Blockchain:
    def __init__(self):
        self.transactions = []
        self.chain = []
        self.create_genesis_block(previous_hash='0')

    def add_block_to_chain(self, block):
        self.chain.append(block)
        self.transactions = []

    def create_genesis_block(self, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'nonce': 1,
            'hash': '0000genesis_hash',
            'transactions_number': len(self.transactions),
            'transactions': self.transactions,
            'timestamp': str(datetime.datetime.now()),
            'previous_hash': previous_hash
        }

        self.add_block_to_chain(block)

    def get_previous_block(self):
        return self.chain[-1]

    def get_block(self, nonce):
        return {
            'index': len(self.chain) + 1,
            'nonce': nonce,
            'transactions_number': len(self.transactions),
            'transactions': self.transactions,
            'timestamp': str(datetime.datetime.now()),
            'previous_hash': self.get_previous_block()['hash']
        }

    def encrypt_data(self, block):
        """ Encrypts block data into 64 bits word """
        return hashlib.sha256(json.dumps(block).encode()).hexdigest()

    def create_transactions(self):
        """ A transaction is defined by a sender, a receiver and the value of the transaction """
        """ In this cause we will only be considering the transaction hash """
        for i in range(random.randint(3,10)):
            transaction = {
                'hash': self.encrypt_data(str(datetime.datetime.now()) + str(i)),
                'joeCoins': random.randint(1,10)
            }

            self.transactions.append(transaction)

    def mine_block(self):
        """ Nonce is the one of the values that will allow the user to mine a block """
        nonce = 1
        check_hash = False

        while check_hash is False:
            """ Block information """
            block = self.get_block(nonce)

            """ Block hash represents all the data encrypted as a unique 64 bits word """
            block_hash = self.encrypt_data(block)

            """ Check if the block hash is in target range """
            target = '0000'
            if block_hash[:4] == target:
                check_hash = True
                block['hash'] = block_hash
            else:
                """ Increment nonce to change the block encription """
                nonce += 1

        return block

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            block = chain[block_index]

            if block['previous_hash'] != self.hash(previous_block):
                return False

            block_hash = self.encrypt_data(previous_block)

            target = '0000'

            if block_hash != target:
                return False

            previous_block = block
            block_index += 1

        return True





