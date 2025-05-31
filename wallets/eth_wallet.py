# wallets/eth_wallet.py

from eth_account import Account

def generate_eth_wallet():
    acct = Account.create()
    return {
        'address': acct.address,
        'private_key': acct.key.hex()
    }
