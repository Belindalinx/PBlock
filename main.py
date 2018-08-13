#initializing blockchain as a list
MINING_REWARD = 10
GENESIS_BLOCK = {"pre_hash": "", "index": 0, "txs": []}
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
Q. Quit
H. Hack
    """)
    choice = input("choose a function you want: ")
    return choice

#hash a block
def hash_block(block):
    return "-".join([str(block[i]) for i in block])

#get last blockchain value
def pre_led():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

#block mining
def op_block():
    pre_block = blockchain[-1]
    hashed_block = hash_block(pre_block)

    re_tx = {"sender": "Mining",
             "recipient": owner,
             "amt": MINING_REWARD}

    copied_txs = op_txs[:]
    copied_txs.append(re_tx)

    block = {"pre_hash": hashed_block,
             "index": len(blockchain),
             "txs": copied_txs}

    blockchain.append(block)
    return True


#get balance
def balance(participant):
    tx_sender = [[tx["amt"] for tx in block["txs"] if tx["sender"] == participant] for block in blockchain]
    op_tx_sender = [tx["amt"] for tx in op_txs if tx["sender"] == participant]
    tx_sender.append(op_tx_sender)

    sent_amt = 0
    for tx in tx_sender:
        if len(tx) > 0:
            sent_amt += tx[0]

    tx_recipient = [[tx["amt"] for tx in block["txs"] if tx["recipient"] == participant] for block in blockchain]

    receive_amt = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            receive_amt += tx[0]

    return receive_amt - sent_amt


#get a new transaction data such as recipient and amount
def tx_data():
    tx_recipient = input("Who is the recipient ? :")
    tx_amt = float(input("your transaction amount?"))
    return tx_recipient, tx_amt

#add transaction data in to the transaction list
def add_tx(recipient, sender=owner, amt=1):
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



#verify the chain to make sure the ledger not be hacked
def verify_chain():
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block["pre_hash"] != hash_block(blockchain[index - 1]):
            return False
    return True

"""
    #block_index=0
    valid=True
    for block_index in range(len(blockchain)):
    #for block in blockchain:
        if block_index==0:
            #block_index+=1
            continue
        #elif block[0]==blockchain[block_index-1]:
        elif blockchain[block_index][0]==blockchain[block_index-1]:
            valid=True
        else:
            valid=False
            break
        #block_index+=1
    return valid    
"""

#main
def main():
    choice = ""
    while choice not in ["q","Q"]:
        choice = menu()

        if choice.upper() == "Q":
            print("Good Bye")

        elif choice == "1":
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

        print(balance("B"))

    return

main()
