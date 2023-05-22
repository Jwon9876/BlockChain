# main.py
from app.blockchain import Blockchain

def main():
    # Blockchain 생성자를 이용해 인스턴스를 생성하고, 필요한 인자를 전달합니다.
    bitcoin = Blockchain()

    # previous_block_hash = '519619156945694516'
    # current_block_data = [
    #     {
    #         'amount' : 10,
    #         'sender' : 'BAD48461AB6',
    #         'recipient' : 'ag4a6e4g9a4w5eg',
    #     },
    #     {
    #         'amount' : 30,
    #         "sender" : '15DSGA86G4AD46GAE',
    #         'recipient' : 'aega6we16ga1we65g1',
    #     },
    #     {
    #         'amount' : 100,
    #         "sender" : 'GAWEKGAWE66GA16W1E1661',
    #         'recipient' : 'a6w191a9be156b1a',
    #     },
    # ]
    # nonce = 100


    bc1 =     { "chain" :
	[
		{
			"hash": "f0020ca0b036c8bd0fc3ce1103bdb04912d654491d6e831ca24c591ddf6e53d6",
			"index": 1,
			"merkle_root": "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b",
			"nonce": 778,
			"previous_block_hash": "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9",
			"timestamp": 1684737771477,
			"transactions": [
				{
					"amount": 50,
					"recipient": "d34ed5c69ef24055af0084667330bf4f",
					"sender": "0",
					"transaction_id": "2b628d821ae94bf784be1390de2a4662"
				}
			]
		}
	],
		"current_node_url"
:
	"http://localhost:5000",
		"genesis_nonce"
:
	778,
		"merkle_tree_proecss"
:
	[],
		"network_nodes"
:
	[],
		"pending_transactions"
:
	[
		{
			"amount": 6.25,
			"recipient": "00",
			"sender": "00",
			"transaction_id": "f73dbee767d54c03a2993cce409ad3f5"
		}
	]
}
    


    

    print('VALID:', bitcoin.chain_is_valid(bc1['chain']))
    #print(bitcoin.hash_block(previous_block_hash,current_block_data,900))

if __name__ == "__main__":
    main()
