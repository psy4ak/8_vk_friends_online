import vk
import getpass


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
    return api.users.get(user_ids=friends_online_id)


def output_friends_to_console(friends_online):
    print('Список друзей онлайн:')
    for count, friend in enumerate(friends_online, start=1):
            print('%s. %s %s' % (count, friend['first_name'],
                  friend['last_name']))

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
