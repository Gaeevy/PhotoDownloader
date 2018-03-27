import vk
import pickle

app_id = '5979581'
login = 'mylogin'
password = 'mypassword'
v = 5.0

session = vk.AuthSession(app_id, login, password, scope='wall, messages')
vkapi = vk.API(session)


def getAllChats(vkapi, chats_backup='chats.pickle'):
    chats_count = vkapi.messages.getDialogs(v=v)['count']
    offset = 0
    resid = chats_count
    raw_chats = list()
    while offset < chats_count:
        print('{} chats are remaining'.format(resid))
        raw_chats += vkapi.messages.getDialogs(count=200, offset=offset, v=v)['items']
        offset += 200
        resid -= 200

    chats = list()

    for chat in raw_chats:
        if 'chat_id' in chat:
            chats.append({'type': 'chat', 'id': chat['chat_id']})
        else:
            chats.append({'type': 'dialog', 'id': chat['user_id']})

    with open(chats_backup, 'wb') as f:
        pickle.dump(chats, f)

    return chats