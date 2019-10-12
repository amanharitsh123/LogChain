from web3 import Web3
infura_url = "https://mainnet.infura.io/v3/ff9137b012f144d7996e8957fb2f5b26"

web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())

balance = web3.eth.getBalance("0xA469FbEED8499A929c0E63aeb5F58951CF616D9b")
print(balance)
print(web3.fromWei(balance,'ether'))
