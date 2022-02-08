#!/bin/bash

# Mint specific item from the collection to default wallet.
# The number here comes from the NFTmaker pro database of tokens
python3 mint_specific.py -s 5568169

# Mint specific item from the collection to new wallet (for example if you want to mint/send directly to a team member)
python3 mint_specific.py -s 5568169 -w addr1q82qg32blahblahblahblahblahblahblahblahblah

# Mint random token and send to default wallet
python3 mint_specific.py -r

# Mint random token and send to specific wallet
python3 mint_specific.py -r -w addr1q82qg32blahblahblahblahblahblahblahblahblah