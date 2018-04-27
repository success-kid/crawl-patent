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
filename = "training.tar.gz"
blob = bucket.get_blob("python_download_description.7z")
blob.download_to_filename("python_download_description.7z")
