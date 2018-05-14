from google.cloud import storage
import os
import platform
import sys



if 'GOOGLE_APPLICATION_CREDENTIALS' not in os.environ:
    if platform.system() == "Windows":
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C:\GCP\Project-d23421f021e1.json"
    else:
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/jeremy455576/GCP/Project-d23421f021e1.json"
        
storage_client = storage.Client() 
bucket = storage_client.get_bucket("patent-specification")
# filename = "training.tar.gz"
for f in sys.argv[1:]:
	print(f, "starts")
	CHUNK_SIZE = 10485760 
	blob = bucket.blob(f, chunk_size=CHUNK_SIZE)
	if blob.exists():
		print("file exists on GCP storage, please change filename!")
	else:		
		blob.upload_from_filename(f)
	
