import json
from web3 import Web3

ganache_url = 'http://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))
web3.eth.defaultAccount = web3.eth.accounts[0]

abi = json.load(open('abi.json'))
# print(abi)
address = "0x3A81Ba31663723FFA2f13992266b2b7E6298Fe8c"
address = web3.toChecksumAddress(address)
contract = web3.eth.contract(address=address,abi=abi)
# Read data from smart contract
print(contract.functions.greet().call())

# Write data
tx_hash = contract.functions.setGreeting('Hi2 Aman').transact()
print(tx_hash)
print(contract.functions.greet().call())
 