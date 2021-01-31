import datetime
import json
import pymongo
import requests_oauthlib 
import tqdm 
# 追記
from dotenv import load_dotenv
import os
from os.path import join, dirname

# 環境変数を.envファイルから取得
dotenv_path = join(dirname('../'+__file__), '.env')
load_dotenv(dotenv_path)

# キー、トークン
API_KEY             = os.environ.get('API_key')
API_SECRET_KEY      = os.environ.get('API_secret_key')
ACCESS_TOKEN        = os.environ.get('Access_token')
ACCESS_TOKEN_SECRET = os.environ.get('Access_token_secret')

# セッション作成/開始
twitter = requests_oauthlib.OAuth1Session(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# 全ツイートの一部をランダムに取得するAPI
url = 'https://stream.twitter.com/1.1/statuses/sample.json'
"""
Returns a small random sample of all public statuses. 
The Tweets returned by the default access level are the same, 
so if two different clients connect to this endpoint, 
they will see the same Tweets.
すべての公開状態の小さなランダムサンプルを返します。
デフォルトのアクセスレベルで返されるツイートは同じなので、
2つの異なるクライアントがこのエンドポイントに接続しても、
同じツイートが表示されます。
"""

# ツイート取得
req = twitter.get(
                url, 
                # data=dict({'track':データベース})
                stream=True) # 

# reqオブジェクトが持つステータスコードが200番台以外だったら、例外を起こす
req.raise_for_status() 

mongo = pymongo.MongoClient()
for line in tqdm.tqdm(req.iter_lines(), unit='tweets', mininterval=1):
    if line:
        tweet = json.loads(line)
        tweet['_timestamp'] = datetime.datetime.utcnow().isoformat()
        # twitterデータベースのsampleコレクション(RDBでいうテーブル)にツイートデータを挿入
        mongo.twitter.sample.insert_one(tweet)