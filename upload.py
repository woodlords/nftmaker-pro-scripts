import requests
import base64
import json
from pprint import pprint
import argparse


p = argparse.ArgumentParser(description="New")
p.add_argument('-f','--folder-name', required=True, help='Folder name of the images/metadata files')
p.add_argument('-s','--start', required=False, help='Start ID to upload')
p.add_argument('-e','--end', required=False, help='End number for IDs to upload')
p.add_argument('--ids', nargs="+", required=False, help='List of local IDs to upload')
args = p.parse_args()


# Some variables you will need
api_key = "api_key_from_nftmakerpro"
nft_project_id = "12345"
upload_url = f'https://api.nft-maker.io/UploadNft/{api_key}/{nft_project_id}'
prefixName="WoodCastleProject"
prefixDispalyName="Wood Castle: Wood Lords S1 " # Leave a space at the end as we will add the #number of token at the end.
projectDescription="Wood Castle Studios Presents Woods Lords: Season One"

# Lord details
folder_name = args.folder_name
ids_list = args.ids

def convert_image_to_base64(image_file):
    with open(image_file, 'rb') as binary_file:
        binary_file_data = binary_file.read()
        base64_encoded_data = base64.b64encode(binary_file_data)
        base64_message = base64_encoded_data.decode('utf-8')
    return base64_message


# See example Metadata file to use for adding metadata
def gen_api_metadata(metadata_json_file):
    api_metadata = 'api_' + metadata_json_file
    with open(metadata_json_file, 'r') as fd:
        myjson = json.load(fd)
    data = []
    for k,v in myjson.items():
        d = { }
        d['name'] = k
        d['value'] = v
        data.append(d)
    return data


def gen_metadata(assetName):
    metadata_file = "images/" + folder_name + '/' +  assetName + '.json'
    image_file = "images/" + folder_name + '/' +  assetName + '.jpg'
    base64_message = convert_image_to_base64(image_file)
    api_metadata = gen_api_metadata(metadata_file)
    params = {
        "assetName": prefixName+assetName, # If you set up a prefix in your project, you omit the prefix here, if not add prefix as well
        "previewImageNft": {
            "mimetype": "image/jpeg",
            "displayname": prefixDispalyName + "#" + assetName,
            "fileFromBase64": base64_message,
            "description": projectDescription,
            "metadataPlaceholder": api_metadata
        }
    }
    return params


def upload_image(data):
    try:
        r = requests.post(upload_url, json=data)
        print(r.json())
    except:
        print(str(i) + ' : FAILED!')


def upload_set(startCount, endCount):
    # Names of the images/metadata files
    for i in range(startCount, endCount+1):
        if(i < 10):
            assetName = '000' + str(i)
        elif(i < 100):
            assetName = '00' + str(i)
        elif(i < 1000):
            assetName = '0' + str(i)
        else:
            assetName = str(i)
        print(f'INFO: Working on asset {prefixName+assetName}')
        data = gen_metadata(assetName)
        upload_image(data)


def main():
    # Iterate through list of IDs and upload them
    if args.ids:
        for i in args.ids:
            startCount = int(i)
            endCount = int(i)
            upload_set(startCount,endCount)

    else:
        startCount = int(args.start)
        endCount = int(args.end)
        upload_set(startCount,endCount)


main()

