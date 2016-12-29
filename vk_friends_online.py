import vk
import getpass
import time


APP_ID = 5798463


def get_user_login():
    user_login = input('Введите логин пользователя VK: ')
    return user_login


def get_user_password():
    user_password = getpass.getpass('Введите пароль пользователя VK: ')
    return user_password


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends',
    )
    api = vk.API(session)
    friends_online_id = api.friends.getOnline()
    friends_online_name = []
    for friend in friends_online_id:
        get_user = api.users.get(user_ids=friend)
        get_user = get_user[0]
        online_name = get_user['first_name'] + ' ' + get_user['last_name']
        friends_online_name.append(online_name)
        time.sleep(0.33)
    return friends_online_name


def output_friends_to_console(friends_online):
    print('Друзья online: ', friends_online)

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
