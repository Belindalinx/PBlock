#initializing blockchain as a list
blockchain=[]

#get last blockchain value
def pre_gl():
    return blockchain[-1]

#enter a new value
def tx_amt():
    tx_amt=float(input("your transaction amount?"))
    return tx_amt

#function for add value
def add_value(tx, last_tx=0):
    blockchain.append([last_tx, tx])
    return blockchain

#main
def main():
    add_value(tx_amt())

    while True:
        add_value(tx_amt(), pre_gl())

        for block in blockchain:
            print(block)
    return

main()
