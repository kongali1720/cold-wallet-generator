# main.py

from wallets.btc_wallet import generate_btc_wallet
from wallets.eth_wallet import generate_eth_wallet
from wallets.doge_wallet import generate_doge_wallet

from utils.qr_generator import create_qr
from utils.pdf_exporter import export_wallet_pdf

def main():
    print("=== Cold Wallet Generator ===")
    print("[1] Bitcoin")
    print("[2] Ethereum")
    print("[3] Dogecoin")
    choice = input("Pilih jenis wallet: ")

    if choice == '1':
        wallet = generate_btc_wallet()
    elif choice == '2':
        wallet = generate_eth_wallet()
    elif choice == '3':
        wallet = generate_doge_wallet()
    else:
        print("Pilihan tidak valid.")
        return

    print("\n[+] Address:", wallet['address'])
    print("[+] Private Key:", wallet['private_key'])

    # Buat QR code
    create_qr(wallet['address'], 'address.png')
    create_qr(wallet['private_key'], 'private_key.png')

    # Buat PDF backup
    export_wallet_pdf(wallet)

if __name__ == "__main__":
    main()
