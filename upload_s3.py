import boto
from boto.s3.key import Key
import json
import sys

with open("pwd.json", 'r', encoding='utf8') as f:
    pwd_data = json.load(f)
AWS_ACCESS_KEY_ID = pwd_data['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = pwd_data['AWS_SECRET_ACCESS_KEY']
bucket_name = pwd_data['S3_BUCKET']

conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
bucket = conn.get_bucket(bucket_name)
k = Key(bucket)

for f in sys.argv[1:]:
    print(f, 'started')
    k.key = "patent/" + f
    k.set_contents_from_filename(f)