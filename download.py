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
# filename = "python_download_description.7z"
for f in sys.argv[1:]:
	filename = sys.argv[0]
	if filename in os.listdir():
		print(filename + " exists, please change local filename!")
	else:
		blob = bucket.get_blob(filename)
		blob.download_to_filename(filename)



