# import boto3
# import json

# with open("pwd.json", 'r', encoding="utf8") as f:
#     pwd_data = json.load(f)
# ACCESS_KEY = pwd_data['ACCESS_KEY']
# SECRET_KEY = pwd_data['SECRET_KEY']
# SESSION_TOKEN = pwd_data['SESSION_TOKEN']

# client = boto3.client(
#     's3',
#     aws_access_key_id=ACCESS_KEY,
#     aws_secret_access_key=SECRET_KEY,
#     aws_session_token=SESSION_TOKEN,
# )

# client.upload_file('/tmp/hello.txt', 'mybucket', 'hello.txt')

# Imports the Google Cloud client library


from google.cloud import storage
import os
import platform

if 'GOOGLE_APPLICATION_CREDENTIALS' not in os.environ:
    if platform.system() == "Windows":
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C:\GCP\Project-d23421f021e1.json"
    else:
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/jeremy455576/GCP/Project-d23421f021e1.json"
        
storage_client = storage.Client()
bucket = storage_client.get_bucket("patent-specification")
# print(list(bucket.list_blobs()))
datadir = os.path.join("training", 'python_download_description')
dirs = os.listdir(datadir)
for d in dirs:
    print(d, "dir start!")
    files = os.listdir(os.path.join(datadir, d))
    for f in files:
        g_path = os.path.join(d, f).replace('\\', '/')
        blob = bucket.blob(g_path)
        path = os.path.join(datadir, d, f)
        blob.upload_from_filename(path)