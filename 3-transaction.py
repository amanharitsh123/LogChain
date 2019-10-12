from web3 import Web3

ganache_url = 'http://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))

# print(web3.eth.blockNumber)
# Transaction between two accounts
account_1 = "0x8409F9fe2f0d50d733008341a0353fD73F7DdEB5"
account_2 = "0x0cC6049346B0ce94a619584398f47a75716dCB5a"

private_key = "ab11752edf03912516d2d7662edbd6ca3d17b65459d832ca6e16b98f1b79142c"

# Get the nounce
nonce = web3.eth.getTransactionCount(account_1)
# build a transaction

tx = {
    'nonce': nonce, # Prevention from sending transaction twice
    'to': account_2,
    'value': web3.toWei(1,'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50','gwei')
}

# Sign the transaction

signed_tx = web3.eth.account.signTransaction(tx,private_key)
# send the transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
# Get transaction hash
print(tx_hash)
