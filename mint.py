import requests
import base64
import json
from pprint import pprint
import argparse

p = argparse.ArgumentParser(description="New")
p.add_argument('-s','--specific', help='specific token')
p.add_argument('-r','--random', action='store_true', required=False)
p.add_argument('-w','--wallet', help='wallet address to send to')

args = p.parse_args()

# Upload URL
api_key = "api_key_from_nftmakerpro"
nft_project_id = "12345"
mint_url = f'https://api.nft-maker.io/MintAndSendSpecific/{api_key}/{nft_project_id}'
mint_random_url = f'https://api.nft-maker.io/MintAndSendRandom/{api_key}/{nft_project_id}'
# Artist wallet address
mywallet_address = 'Replace_with_CardanoWalletAddress'


def mint_specific(nft_server_id, receiver_address, count=1):
    url = f"{mint_url}/{nft_server_id}/{count}/{receiver_address}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f'Successfully Minted NFT {nft_server_id}')
        else:
            print(f'Mint command failed with {response.status_code}')
    except:
        print(response.text)
        raise


def mint_random(receiver_address, count=1):
    url = f"{mint_random_url}/{count}/{receiver_address}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f'Successfully Minted Random NFT {response.status_code}')
        else:
            print(f'Mint command failed with {response.status_code}')
    except:
        print(response)
        raise


def main():
    if args.wallet:
        wallet_address = args.wallet
    else:
        wallet_address = mywallet_address

    print(f'INFO: Using wallet address {wallet_address}')

    if args.specific:
        mint_specific(args.specific, wallet_address)
    if args.random:
        mint_random(wallet_address)


main()