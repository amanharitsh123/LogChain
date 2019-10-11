from web3 import Web3
infura_url = "https://mainnet.infura.io/v3/ff9137b012f144d7996e8957fb2f5b26"

web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())

balance = web3.eth.getBalance("")

