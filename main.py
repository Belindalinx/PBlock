import hashlib as h
import json
import functools

#initializing blockchain as a list
MINING_REWARD = 10
GENESIS_BLOCK = {"pre_hash": "",
                 "index": 0,
                 "txs": [],
                 "proof": 100
                 }
blockchain = [GENESIS_BLOCK]
op_txs = []
owner = "B"
participants = {"B"}

#display blockchain
def display_block():
    for block in blockchain:
        print("Block display")
        print(block)
    else:
        print("-"*20)
    return

#the function menu to interacte with user
def menu():
    print("""
Menu:
1. Add a new transaction
2. Display the block
3. Mine a new block
4. Show participants
5. Check transaction validity
Q. Quit
H. Hack
    """)
    choice = input("choose a function you want: ")
    return choice

#hash a block
def hash_block(block):
    return h.sha256(json.dumps(block).encode()).hexdigest()

def valid_proof(txs, pre_hash, proof):
    guess = (str(txs) + str(pre_hash) + str(proof)).encode()
    hashed_guess = h.sha256(guess).hexdigest()
    print(hashed_guess)
    return hashed_guess[0:2] == "00"

def pow():
    pre_block = blockchain[-1]
    hashed_block = hash_block(pre_block)
    proof = 0
    while valid_proof(op_txs, hashed_block, proof):
        proof += 1
    return proof


#block mining
def op_block():
    pre_block = blockchain[-1]
    hashed_block = hash_block(pre_block)

    proof = pow()

    re_tx = {"sender": "Mining",
             "recipient": owner,
             "amt": MINING_REWARD}

    copied_txs = op_txs[:]
    copied_txs.append(re_tx)

    block = {"pre_hash": hashed_block,
             "index": len(blockchain),
             "txs": copied_txs,
             "proof": proof
             }

    blockchain.append(block)
    return True

#get last blockchain value
def pre_led():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


#get balance
def balance(participant):
    tx_sender = [[tx["amt"] for tx in block["txs"] if tx["sender"] == participant] for block in blockchain]
    op_tx_sender = [tx["amt"] for tx in op_txs if tx["sender"] == participant]
    tx_sender.append(op_tx_sender)

    print(tx_sender)
    sent_amt = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)
    """
    sent_amt = 0
    for tx in tx_sender:
        if len(tx) > 0:
            sent_amt += tx[0]
    """

    tx_recipient = [[tx["amt"] for tx in block["txs"] if tx["recipient"] == participant] for block in blockchain]

    receive_amt = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_recipient, 0)
    """
    receive_amt = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            receive_amt += tx[0]
    """

    return receive_amt - sent_amt


#get a new transaction data such as recipient and amount
def tx_data():
    tx_recipient = input("Who is the recipient ? :")
    tx_amt = float(input("your transaction amount?"))
    return tx_recipient, tx_amt

#add transaction data in to the transaction list
def add_tx(recipient, sender=owner, amt=1.0):

    tx = {"sender": sender,
          "recipient": recipient,
          "amt": amt}

    if verify_tx(tx):
        op_txs.append(tx)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def verify_tx(tx):
    sender_balance = balance(tx["sender"])
    return sender_balance >= tx["amt"]

def verify_txs():
    return all([verify_tx(tx) for tx in op_txs])

#verify the chain to make sure the ledger not be hacked
def verify_chain():
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block["pre_hash"] != hash_block(blockchain[index - 1]):
            return False
    return True


#main
def main():
    choice = ""
    while choice not in ["q","Q"]:
        choice = menu()

        if choice.upper() == "Q":
            print("Good Bye")

        elif choice == "1":
            global op_txs
            new_tx = tx_data()
            recipient, amt = new_tx
            if add_tx(recipient, amt=amt):
                print("transaction added")
            else:
                print("transaction failed")
            print(op_txs)

        elif choice == "2":
            display_block()

        elif choice == "3":
            if op_block():
                op_txs = []

        elif choice == "4":
            print(participants)

        elif choice == "5":
            if verify_txs():
                print("All txs are valid")
            else:
                print("There are invalid txs")

        elif choice == "h":
            if len(blockchain) >= 1:
                blockchain[0] = {"pre_hash": "", "index": 0,
                                 "txs": [
                                     {"sender": "B",
                                      "recipient": "a",
                                      "amt": 100}
                                        ]
                                }

        else:
            print(choice, "is a invalid choice")

        if not verify_chain():
            display_block()
            print("Invalid ledger")
            break

        print("Balance of {} :{:6.2f} ".format("B", balance("B")))

    return

main()
