import vk
import time
import pickle

app_id = '5979581'
login = 'mylogin'
password = 'mypassword'
v = 5.0

session = vk.AuthSession(app_id, login, password, scope='wall, messages')
vkapi = vk.API(session)


def getChatHistory(vkapi, v, chat, sleep_time=0.55):
    id = chat['id']
    mes_history = []
    if chat['type'] == 'dialog':
        mess_count = vkapi.messages.getDialogs(user_id=id, v=v)['count']
        resid = mess_count
        offset = 0
        while offset < mess_count:
            print('--processing user', id, ':', resid, 'of', mess_count, 'messages left')
            mes_history += vkapi.messages.getHistory(user_id=id, count=200, offset=offset, v=v)['items']
            time.sleep(sleep_time)
            resid -= 200
            offset += 200
    else:
        mess_count = vkapi.messages.getDialogs(chat_id=id, v=v)['count']
        resid = mess_count
        offset = 0
        while offset < mess_count:
            print('--processing chat', id, ':', resid, 'of', mess_count, 'messages left')
            mes_history += vkapi.messages.getHistory(chat_id=id, count=200, offset=offset, v=v)['items']
            time.sleep(sleep_time)
            resid -= 200
            offset += 200
    return mes_history


with open('chats.pickle', 'rb') as f:
    chats = pickle.load(f)

cur_chat = 0
chat_count = len(chats)
for i in range(447, chat_count):
    print('-------------------------------', chat_count - i, 'CHATS ARE LEFT --------------------------------')
    chat = chats[i]
    file_name = 'messages/' + str(chat['id']) + chat['type']
    mes = getChatHistory(vkapi, v, chat)
    with open(file_name, 'wb') as f:
        pickle.dump(mes, f)