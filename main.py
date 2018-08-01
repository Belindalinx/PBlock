#initializing blockchain as a list
blockchain=[]

#get last blockchain value
def pre_led():
    if len(blockchain)<1:
        return None
    return blockchain[-1]

#enter a new value
def tx_amt():
    tx_amt=float(input("your transaction amount?"))
    return tx_amt

#function for add value
def add_tx(tx, last_tx):
    if last_tx==None:
        last_tx=[0]
    blockchain.append([last_tx, tx])
    return blockchain

#verify the chain to make sure the ledger not be hacked
def verify():
    block_index=0
    valid=True
    for block in blockchain:
        if block_index==0:
            block_index+=1
            continue
        elif block[0]==blockchain[block_index-1]:
            valid=True
        else:
            valid=False
            break
        block_index+=1
    return valid

#display blockchain
def display_block():
    for block in blockchain:
        print(block)
    return

def menu():
    print("""
Menu:
1. Add a new transaction"
2. Display the block"
Q. Quit
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
            new_tx=tx_amt()
            add_tx(new_tx, pre_led())

        elif choice=="2":
            display_block()

        else:
            print(choice, "is a invalid choice")

        if not verify():
            print("Invalid ledger")
            break

    return

main()
