from pymongo import MongoClient
import certifi
from web3 import Web3
from dotenv import load_dotenv
load_dotenv()
import os


def database(email,cro_address,ip_address,submission_id):
    try:
        cluster = MongoClient(f"mongodb+srv://titanmaker:cVCoBFY6TluS6ClL@cluster0.fdym1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",tlsCAFile=certifi.where())
        db = cluster['titanmaker']
        collection = db['ticket_users']

        # Search for record
        # search_email = collection.find_one({"email":email})
        # search_ip = collection.find_one({"ip":ip_address})
        # search_cro = collection.find_one({"cro_address":cro_address})

        post = {
                "_id":submission_id,
                "email":email,
                "cro_address":cro_address,
                "ip":ip_address
            }

        collection.insert_one(post)
        return True
    except:
        return False

