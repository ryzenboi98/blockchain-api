from flask import Flask, jsonify
from blockchain import Blockchain

app = Flask(__name__)

blockchain = Blockchain()

@app.route('/mine_block', methods = ['GET'])
def mine_block():
    blockchain.create_transactions()

    block = blockchain.mine_block()
    blockchain.add_block_to_chain(block)

    response = {
        'message': 'Congrats! You just mined a block!',
        'index': block['index'],
        'hash': block['hash'],
        'nonce': block['nonce'],
        'transactions_number': block['transactions_number'],
        'timestamp': block['timestamp'],
        'previous_hash': block['previous_hash']
    }

    return jsonify(response), 200

@app.route('/get_chain', methods = ['GET'])
def get_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200