from flask import Flask, jsonify, request
from blockchain import Blockchain

app = Flask(__name__)

blockchain = Blockchain()


@app.route("/mine", methods=["GET"])
def mine():

    last_block = blockchain.last_block()
    previous_hash = blockchain.hash(last_block)

    block = blockchain.create_block(previous_hash)

    return jsonify({
        "message": "New block created",
        "block": block
    })


@app.route("/transaction", methods=["POST"])
def transaction():

    data = request.get_json()

    sender = data["sender"]
    receiver = data["receiver"]
    amount = data["amount"]

    blockchain.add_transaction(sender, receiver, amount)

    return jsonify({
        "message": "Transaction added"
    })


@app.route("/chain", methods=["GET"])
def chain():

    return jsonify({
        "length": len(blockchain.chain),
        "chain": blockchain.chain
    })


if __name__ == "__main__":
    app.run(port=5000)
