import shutil 
from urllib.request import URLopener
opener = URLopener()
import urllib
import requests
from bs4 import BeautifulSoup
import os 
import re
from datetime import datetime

# # create dir for crawled data
# dir_to_be_created = os.path.join('training', 'python_download')
# if 'python_download' not in os.listdir('training'):
#     os.mkdir(dir_to_be_created)
#     print(dir_to_be_created, 'is created')
# else:
#     print(dir_to_be_created, 'already exists')

# # start crawling
# res = requests.get("https://tiponet.tipo.gov.tw/Gazette/OpenData/OD/OD03.aspx?QryDS=P14")
# soup = BeautifulSoup(res.text, 'lxml')
# links = soup.select(".Table02 a")
# numbers = [l.text for l in links]
# print(len(numbers))
# for num in numbers[100:]:
#     print(num)
#     url = 'ftp://s220ftp.tipo.gov.tw/PatentIsuRegSpecXMLB_' + str(num) + '/patent.xml'
#     store_path = 'training//python_download//' + str(num) + '.xml'
#     with opener.open(url) as remote_file, open(store_path, 'wb') as local_file:
#         shutil.copyfileobj(remote_file, local_file)



# create dir for crawled data
dir_to_be_created = os.path.join('training', 'python_download_description')
if 'python_download_description' not in os.listdir('training'):
    os.mkdir(dir_to_be_created)
    print(dir_to_be_created, 'is created')
else:
    print(dir_to_be_created, 'already exists')

# start crawling
def get_ftp_ls(url):
    with urllib.request.urlopen(url) as res :
        try:
            html = res.read()
        except:
            print(url)
            html = ""

    files = html.split(b'\r\n') 
    files = [f.split()[-1] for f in files if len(f.split())>0]
    return files


root_dir = os.path.join('training', 'python_download_description')
res = requests.get("https://tiponet.tipo.gov.tw/Gazette/OpenData/OD/OD03.aspx?QryDS=S01")
soup = BeautifulSoup(res.text, 'lxml')
links = soup.select(".Table02 a")
numbers = [l.text for l in links]
print(len(numbers))
start_num = 2
document_count = 0
for num in numbers[start_num:]:
    print("vol: ", num)
    print("start_num: ", start_num)
    vol_dir = os.path.join(root_dir, str(num))
    if str(num) not in os.listdir(root_dir):
        os.mkdir(vol_dir)

    url_1 = "ftp://s220ftp.tipo.gov.tw/PatentPubXML_" + str(num) + "/"
    files = get_ftp_ls(url_1)
    files = [f.decode() for f in files]
    dirs = [d for d in files if "." not in d]
    print("num of dirs in " + str(num) + " folder: " + str(len(dirs)))
    
    for d in dirs[:]:
        url_2 = url_1 + d + "/"
        files = get_ftp_ls(url_2)
        filename = [f.decode() for f in files if f.lower().endswith(b'.xml')]
        if len(filename) < 1:
            print("fail url:", url_2)
        else:
            filename = filename[0]

            if not filename in os.listdir(vol_dir):
                url_3 = url_2 + filename
                store_path = os.path.join(vol_dir, filename)
                opener = URLopener()
                with opener.open(url_3) as remote_file, open(store_path, 'wb') as local_file:
                    shutil.copyfileobj(remote_file, local_file)

            document_count += 1
            if document_count % 1000 == 0:
                print("num of docs downloaded:", document_count)

    start_num += 1
