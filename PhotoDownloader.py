import pandas as pd
import requests
from os import listdir, makedirs

photos_path = 'photos'
links_path = 'links'
files = listdir(links_path)
file_count = len(files)
resid = file_count

for i in range(0, file_count):
    file = files[i]
    print('------------------', resid, 'CHATS ARE LEFT -------------------------')
    dirpath = photos_path + '/' + file[:file.rfind('.')]
    makedirs(dirpath)
    links = pd.read_csv(links_path + '/' + file)
    for j in range(0, links.shape[0]):
        link = links.iloc[j]['link']
        photo_id = links.iloc[j]['id']
        image = requests.get(link).content
        ext = link[link.rfind('.'):]
        image_name = str(photo_id) + ext
        path = dirpath + '/' + image_name
        with open(path, 'wb') as handler:
            handler.write(image)
        print(str(photo_id) + ' has been written, ' + str(links.shape[0] - j) + ' remaining')
    resid -= 1

