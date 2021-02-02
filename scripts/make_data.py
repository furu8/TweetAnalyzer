import pandas as pd
import numpy as np
import pymongo


# mongodbからデータフレーム作成
mongo = pymongo.MongoClient()
df = pd.DataFrame(list(mongo.twitter.sample.find()))

df.to_csv('../data/twitter_sample.csv', index=False)
# delete_df = df['delete']

# # deleteの中身を抽出
# id_list, id_str_list, user_id_list, user_id_str_list = [], [], [], [] # deleteの中のstatus
# timestamp_ms_list = []                                                # deleteの中のtimestamp_ms
# for delete in delete_df.values:
#     if isinstance(delete, dict):
#         status = delete['status']
#         id_list.append(status['id'])
#         id_str_list.append(status['id_str'])
#         user_id_list.append(status['user_id'])
#         user_id_str_list.append(status['user_id_str'])

#         timestamp_ms = delete['timestamp_ms']
#         timestamp_ms_list.append(timestamp_ms)
#     else:
#         id_list.append(np.nan)
#         id_str_list.append(np.nan)
#         user_id_list.append(np.nan)
#         user_id_str_list.append(np.nan)
#         timestamp_ms_list.append(np.nan)

# # print(df[df['id'].notnull()])
# # print(id_list[:20])
# # deleteの中身をカラムに追加
# df['id'] = id_list
# df['id_str'] = id_str_list
# df['user_id'] = user_id_list
# df['user_id_str'] = user_id_str_list
# df['timestamp_ms'] = timestamp_ms_list

# # delete削除
# df = df.drop('delete', axis=1)

# print(df.columns)