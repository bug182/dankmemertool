import time
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import doers.options as options
import doers.config as config
import doers.spam as spam


def clear():
    os.system('cls')
  

def menu():
    print("1)pls beg")
    print("2)pls gamble")
    print("3)settings")
    choice = input('What would you like to do?:')
    if choice == '1':
        spam.beg()
    elif choice == '2':
        spam.gamble()
    elif choice == '3':
        options.settings()
    else:
        print('thatz not an option silly')
        menu()


if config.first_boot == 'True':
    print("gotta set it up lol")
    with open('doers\config.py') as f:
        boot = f.read().replace('True', 'False')
    with open('doers\config.py', 'w') as f:
        f.write(boot)
    ask_e = input('whats the email?:')
    with open('doers/config.py') as e:
        mail = e.read().replace('email_placeholder', ask_e)
    with open('doers/config.py', 'w') as e:
        e.write(mail)
    print('email set yeet')
    ask_p = input('And the password?:')
    with open('doers\config.py') as p:
        pword = p.read().replace('password_placeholder', ask_p)
    with open('doers\config.py', 'w') as p:
        p.write(pword)
    print('password set')
    ask_c = input('what is the channel url?:')
    with open('doers\config.py') as c:
        chan = c.read().replace('channel_placeholder', ask_c)
    with open('doers\config.py', 'w') as c:
        c.write(chan)
    print('channel added')
    time.sleep(2)
    clear()
    menu()
else:
    print("booted before")
    time.sleep(2)
    clear()
    menu()