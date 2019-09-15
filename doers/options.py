import time
import  doers.config
import os
from importlib import reload

config = doers.config

def settings():
    print('')
    clear = os.system('cls')
    print('1)msg time')
    print('2)gamble amount')
    print('3)account')
    print('4)channel')
    print('5)back')
    choice = input('select option:')
    if choice == '1':
        msg_time()
    elif choice == '2':
        gamble_amount()
    elif choice == '3':
        accounts()
    elif choice == '4':
        channel()
    elif choice == '5':
        import main
        main.menu()
    else:
        print('choose one idiot')
        settings()


def msg_time():
    clear = os.system('cls')
    print('gamble time = ' + str(config.gamble_time))
    print('1)change gamble time')
    print('beg time = ' + str(config.beg_time))
    print('2)chang beg time')
    print('3)back')
    choice = input('choose option:')
    if choice == '1':
        new_time = input('enter new time in seconds(default time=61):')
        with open('doers\config.py', 'r+') as beg:
            timeb = beg.read().replace(str(config.beg_time), new_time)
            beg.write(timeb)
        config = reload(doers.config)
        msg_time()
    elif choice == '2':
        new_time = input('enter new time in second(default time=11):')
        with open('config.py', 'r+') as gamble:
            timeg = gamble.read().replace(str(config.gamble_time), new_time)
            gamble.write(timeg)
        config = reload(doers.config)
        msg_time()
    elif choice == '3':
        settings()
    else:
        print('thats not an option lol')
        time.wait(2)
        msg_time()

def gamble_amount():
    clear = os.system('cls')
    print('current gamble amount = ' + str(config.gamble_amount))
    print('1)change amount')
    print('2)back')
    choice = input('choose option:')
    if choice == '1':
        amount_input = input('how much money?(default = 25):')
        with open('doers\config.py', 'r+') as a:
            amount = a.read().replace(str(config.gamble_amount), amount_input)
            a.write(amount)
        config = reload(doers.config)
        gamble_amount()
    elif choice == '2':
        settings()
    else:
        print('not an op idiot')
        time.wait(2)
        gamble_amount()


def accounts():
    print('current account email = ' + config.email())
    print('1)change account')
    print('2)back')
    choice = input('choose:')
    if choice == '1':
        ask_e = input('whats the email?:')
        with open('doers/config.py') as e:
            mail = e.read().replace(config.email, ask_e)
        with open('doers/config.py', 'w') as e:
            e.write(mail)
        print('email set yeet')
        ask_p = input('And the password?')
        with open('doers\config.py') as p:
            pword = p.read().replace(config.password, ask_p)
        with open('doers\config.py', 'w') as p:
            p.write(pword)
        print('email set')
        config = reload(doers.config)
        accounts()
    elif choice == '2':
        settings()
    else:
        print('thats not an option numbnuts')
        accounts()


def channel():
    config = reload(doers.config)
    os.system('clear')
    print('current channel url = ' + config.channel)
    print('1)change channel')
    print('2)back')
    choice = input('choose:')
    if choice == '1':
        ask_c = input('new channel url:')
        with open('doers/config.py') as c:
            chan = c.read().replace(config.channel, ask_c)
        with open('doers/config.py', 'w') as c:
            c.write(chan)
        config = reload(doers.config)
        channel()
    elif choice == '2':
        settings()
    else:
        print('thats not an option numbnuts')