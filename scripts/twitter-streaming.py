import datetime
import json
import pymongo
import requests_oauthlib
import tqdm

from dotenv import load_dotenv
import os
from os.path import join, dirname

dotenv_path = join(dirname('../'+__file__), '.env')
load_dotenv(dotenv_path)

# 環境変数
API_KEY             = os.environ.get('API_key')
API_SECRET_KEY      = os.environ.get('API_secret_key')
ACCESS_TOKEN        = os.environ.get('Access_token')
ACCESS_TOKEN_SECRET = os.environ.get('Access_token_secret')

twitter = requests_oauthlib.OAuth1Session(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
url = 'https://stream.twitter.com/1.1/statuses/sample.json'
req = twitter.get(url, stream=True)
req.raise_for_status()

mongo = pymongo.MongoClient()
for line in tqdm.tqdm(req.iter_lines(), unit='tweets', mininterval=1):
    if line:
        tweet = json.loads(line)
        tweet['_timestamp'] = datetime.datetime.utcnow().isoformat()
        mongo.twitter.sample.insert_one(tweet)