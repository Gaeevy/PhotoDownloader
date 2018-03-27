import pickle
import pandas as pd
from os import listdir
from os.path import isfile, join

PHOTO = 'photo'
ATTACHMENTS = 'attachments'
FWD_MESSAGES = 'fwd_messages'
ID = 'id'
TYPE = 'type'


def findLargestPhotoKey(photoKeys):
    size = 0
    for photoKey in photoKeys:
        if PHOTO in photoKey:
            curSize = int(photoKey[photoKey.index('_')+1:])
            if curSize > size:
                size = curSize
    return 'photo_{}'.format(size)


def messageProcess(message):
    photos = list()
    if FWD_MESSAGES in message:
        fwd_messages = message[FWD_MESSAGES]
        for fwd_message in fwd_messages:
            photos += messageProcess(fwd_message)
    if ATTACHMENTS in message:
        attachments = message[ATTACHMENTS]
        for attachment in attachments:
            if attachment[TYPE] == PHOTO:
                photo = attachment[PHOTO]
                photo_id = photo[ID]
                keys = photo.keys()
                bestPhoto = findLargestPhotoKey(keys)
                photos.append({'id': photo_id, 'link': photo[bestPhoto]})
    return photos


def findPhotos(messages):
    photos = list()
    for message in messages:
        photos += messageProcess(message)
    return photos


mess_path = 'messages'
files = listdir(mess_path)
file_count = len(files)
resid = file_count

for i in range(0, file_count):
    print('---------------', resid, ' FILES ARE LEFT')
    file = files[i]
    with open('messages/' + file, 'rb') as f:
        messages = pickle.load(f)

    photos = findPhotos(messages)
    if photos:
        df = pd.DataFrame(photos)
        file_name = 'links/' + file + '.csv'
        df.to_csv(file_name, index=False)
    resid -= 1


