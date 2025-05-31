# wallets/btc_wallet.py

import os
import hashlib
import ecdsa
import base58

def generate_btc_wallet():
    # 1. Generate Private Key (32 bytes hex)
    private_key = os.urandom(32).hex()

    # 2. Generate Public Key
    sk = ecdsa.SigningKey.from_string(bytes.fromhex(private_key), curve=ecdsa.SECP256k1)
    vk = sk.verifying_key
    public_key = b'\x04' + vk.to_string()  # uncompressed format

    # 3. Hashing Public Key -> Address
    sha256_pk = hashlib.sha256(public_key).digest()
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(sha256_pk)
    hashed_pk = ripemd160.digest()

    # 4. Add network byte (0x00 for Mainnet BTC)
    network_byte = b'\x00' + hashed_pk

    # 5. Checksum
    checksum = hashlib.sha256(hashlib.sha256(network_byte).digest()).digest()[:4]

    # 6. Address (Base58)
    address = base58.b58encode(network_byte + checksum).decode()

    # 7. Convert Private Key to WIF
    wif_prefix = b'\x80' + bytes.fromhex(private_key)
    wif_checksum = hashlib.sha256(hashlib.sha256(wif_prefix).digest()).digest()[:4]
    wif = base58.b58encode(wif_prefix + wif_checksum).decode()

    return {
        'address': address,
        'private_key': wif
    }
