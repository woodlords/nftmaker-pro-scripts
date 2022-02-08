# nftmaker-pro-scripts
Helper scripts for NFTMaker Pro


# Setup
You will need few variables such a `api_key` & `nft_project_id` you can get these from the NFTmaker UI. `prefixName` is the prefix of your project name. This will be used to create the NFTs.

## Images Setup
Images and metadata should be added to the images folder, you can use the `folder_name` if you have more than one characters. In the example structre I only have one chracter `morpheus`

## JSON (Metadata files)
Metadata files don't need to be full and rather only the placeholders you will provide based on the project policy you created.


# Uploading
In order to upload you will need to run `upload.py -h` to see the help messages.

```
❯ python3 upload.py -f morpheus --ids 0501
INFO: Working on asset WoodCastleProject0501
```

# Delete
If you made mistakes and you want to deleting a token from the API you can do so with the `delete.py -h` script.


# Minting Token
On the day of mint you might want to mint some random tokens or minting specific tokens with token-ids, you can do that with the `mint.py -h` script.

You can also `mint.py` to mint random token for your team. you just need to add the `-r` flag.

```
# Mint specific item from the collection to default wallet.
# The number here comes from the NFTmaker pro database of tokens
python3 mint_specific.py -s 5568169

# Mint specific item from the collection to new wallet (for example if you want to mint/send directly to a team member)
python3 mint_specific.py -s 5568169 -w addr1q82qg32blahblahblahblahblahblahblahblahblah

# Mint random token and send to default wallet
python3 mint_specific.py -r

# Mint random token and send to specific wallet
python3 mint_specific.py -r -w addr1q82qg32blahblahblahblahblahblahblahblahblah
```
