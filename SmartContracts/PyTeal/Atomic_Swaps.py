#Algorand Atomic Swaps

#Fom 0 to 1
txn_0 = transaction.PaymentTxn(account_0, params, account_1, 40000000)
#From 1 to 2
txn_1 = transaction.PaymentTxn(account_1, params, account_2, 40000000)

#Group
gid = transaction.calculate_group_id([txn_0, txn_1])
txn_0.group = gid
txn_1.group = gid

#Sign
stxn_0 = txn_0.sign(sk_0)    
stxn_1 = txn_1.sign(sk_1)

#Assemble
signed_group =  [stxn_1, stxn_2]

#Send
tx_id = algod_client.send_transactions(signed_group)

#Confirm
wait_for_confirmation(algod_client, tx_id) 
