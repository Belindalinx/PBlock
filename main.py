#initializing blockchain as a list
genesis_block={"pre_hash":"", "index":0, "tx":[]}
blockchain=[genesis_block]
op_tx=[]
owner="B"
participants={"B"}

#hash a block
def hash_block(block):
    return str([block[i] for i in block])

#get last blockchain value
def pre_led():
    if len(blockchain)<1:
        return None
    return blockchain[-1]

#get balance
def balance(participant):
    tx_sender=[[tx["amt"] for tx in block["tx"] if tx["sender"]==participant] for block in blockchain]
    sent_amt=0
    for tx in tx_sender:
        if len(tx)>0:
            sent_amt += tx[0]
    tx_recipient=[[tx["amt"] for tx in block["tx"] if tx["recipient"]==participant] for block in blockchain]
    receive_amt=0
    for tx in tx_recipient:
        if len(tx)>0:
            receive_amt += tx[0]
    return receive_amt-sent_amt



#get a new transaction data such as recipient and amount
def tx_data():
    tx_recipient=input("Who is the recipient ? :")
    tx_amt=float(input("your transaction amount?"))
    return tx_recipient, tx_amt

#add transaction data in to the transaction list
def add_tx(recipient, sender=owner, amt=0):
    tx={"sender":sender, "recipient":recipient, "amt":amt}
    op_tx.append(tx)
    participants.add(sender)
    participants.add(recipient)
    return

#block mining
def op_block():
    pre_block=blockchain[-1]
    hashb=hash_block(pre_block)
    """
    hashb=""
    for i in pre_block:
        value=pre_block[i]
        hashb=str(value)
    """
    block={"pre_hash":hashb, "index":len(blockchain), "tx":op_tx}
    blockchain.append(block)
    return True

#verify the chain to make sure the ledger not be hacked
def verify():
    for (index, block) in enumerate(blockchain):
        if index==0:
            continue
        if block["pre_hash"]!=hash_block(blockchain[index-1]):
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

#display blockchain
def display_block():
    for block in blockchain:
        print(block)
    else:
        print("-"*20)
    return

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
    choice=input("choose a function you want: ")
    return choice

#main
def main():
    choice=""
    while choice not in ["q","Q"]:
        choice=menu()

        if choice.upper()=="Q":
            print("Good Bye")

        elif choice=="1":
            new_tx=tx_data()
            recipient, amt =new_tx
            add_tx(recipient, amt=amt)
            print(op_tx)

        elif choice=="2":
            display_block()

        elif choice=="3":
            if op_block():
                op_tx=[]

        elif choice=="4":
            print(participants)

        elif choice=="h":
            if len(blockchain)>=1:
                blockchain[0]={"pre_hash":"", "index":0,
                               "tx":[{"sender":"B",
                                      "recipient":"a1", "amt":100}]}

        else:
            print(choice, "is a invalid choice")

        if not verify():
            display_block()
            print("Invalid ledger")
            break

        print(balance("a"))

    return

main()