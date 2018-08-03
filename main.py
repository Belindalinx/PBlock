#initializing blockchain as a list
genesis_block={"pre_hash":"", "index":0, "tx":[]}
blockchain=[genesis_block]
op_tx=[]
owner="B"

#get last blockchain value
def pre_led():
    if len(blockchain)<1:
        return None
    return blockchain[-1]

#get a new transaction data such as recipient and amount
def tx_data():
    tx_recipient=input("Who is the recipient ? :")
    tx_amt=float(input("your transaction amount?"))
    return tx_recipient, tx_amt

#add transaction data in to the transaction list
def add_tx(recipient, sender=owner, amt=0):
    tx={"sender":sender, "recipient":recipient, "amt":amt}
    op_tx.append(tx)
    return

#block mining
def op_block():
    pre_block=blockchain[-1]
    hasha=""
    for i in pre_block:
        value=pre_block[i]
        hasha=hasha+str(value)
    block={"pre_hash":hasha, "index":len(blockchain), "tx":op_tx}
    blockchain.append(block)


#verify the chain to make sure the ledger not be hacked
def verify():
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
            op_block()

        elif choice=="h":
            if len(blockchain)>=1:
                blockchain[0]=[2]

        else:
            print(choice, "is a invalid choice")

        #if not verify():
            #display_block()
            #print("Invalid ledger")
            #break

    return

main()
