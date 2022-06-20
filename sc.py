import web3

user_address = ""
pk = ""

contract_addr = ""

Logger_ABI = [
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_run",
                "type": "string"
            }
        ],
        "name": "get",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_run",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_counter",
                "type": "string"
            }
        ],
        "name": "set",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

w3 = web3.Web3(web3.HTTPProvider('http://127.0.0.1:8545'))
print(w3.clientVersion)

store_var_contract = w3.eth.contract(
   address=user_address,
   abi=Logger_ABI)

data_txn = store_var_contract.functions.get("1").buildTransaction({
    'chainId': 1337,
    'gas': 700200,
    'maxFeePerGas': w3.toWei('2', 'gwei'),
    'maxPriorityFeePerGas': w3.toWei('1', 'gwei'),
    'nonce': w3.eth.getTransactionCount(contract_addr)+3
})

signed_txn = w3.eth.account.sign_transaction(data_txn, private_key=pk)
res = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
print(res)
