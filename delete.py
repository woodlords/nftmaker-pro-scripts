from pprint import pprint
import requests
import base64
import json
import argparse
import time
import os
import sys

p = argparse.ArgumentParser(description="Delete NFT")
p.add_argument('--ids', nargs="+", required=False, help='List of local IDs to delete, they should inlcude all 000 zeros based on number of digits.')
p.add_argument('-s','--start', required=False, type=int)
p.add_argument('-e','--end', required=False,type=int)
p.add_argument('-f','--file', required=False)
if len(sys.argv)==1:
    p.print_help(sys.stderr)
    sys.exit(1)
args = p.parse_args()

# Some variables you will need
api_key = "api_key_from_nftmakerpro"
nft_project_id = "12345"
# NFTs uploaded will use this prefix for example
# WoodCastleWLS10001 for token #0001
prefixName="WoodCastleWLS1"
# API URLs
delete_url = f'https://api.nft-maker.io/DeleteNft/{api_key}/{nft_project_id}'
get_url = f'https://api.nft-maker.io/GetNftDetails/{api_key}/{nft_project_id}'


def generate_nftname(local_id, nft_name_prefix=prefixName):
    return nft_name_prefix + str(local_id)


def get_nft_server_id(nftname):
    get_nft_by_name_url = f'{get_url}/{nftname}'
    try:
        results = requests.get(get_nft_by_name_url).json()
        if 'id' in results:
            return results['id']
        else:
            print(f'NFT {nftname} was not found on server, it must have been deleted already')
            return None
    except:
        print(str(results) + ' : FAILED!')
        raise


def delete_nft_by_id(nft_server_id):
    delete_nft_by_id_url = f'{delete_url}/{nft_server_id}'
    try:
        response = requests.get(delete_nft_by_id_url)
        if response.status_code == 200:
            print(f'Deleted Successfully NFT {nft_server_id}')
        else:
            print(f'Delete command failed with {response.text}')
    except:
        print(str(response) + ' : FAILED!')
        raise


def delete(nft_local_id):
    nftname = generate_nftname(nft_local_id)
    print(f'INFO: Deleting NFT {nftname} [{nft_local_id}]')
    nft_server_id = get_nft_server_id(nftname)
    if nft_server_id:
        delete_nft_by_id(nft_server_id)


def gen_local_ids(start,end):
    print('Using Range to build up asset IDs')
    local_ids = []
    for i in range(start, end+1):
        if(i < 10):
            asset_id = '000' + str(i)
        elif(i < 100):
            asset_id = '00' + str(i)
        elif(i < 1000):
            asset_id = '0' + str(i)
        else:
            asset_id = str(i)
        local_ids.append(asset_id)
    return local_ids


def read_file(filepath):
    asset_ids = []
    if os.path.isfile(filepath):
        with open(filepath, 'r') as fd:
            data = fd.readlines()
    for line in data:
        asset_ids.append(line.split('\n')[0])
    return asset_ids


def main():
    if args.start and args.end:
        local_ids = gen_local_ids(args.start, args.end)
    elif args.ids:
        local_ids = args.ids
    elif args.file:
        local_ids = read_file(args.file)
    else:
        print('Error: some args not present')

    for i in local_ids:
        delete(i)


main()


