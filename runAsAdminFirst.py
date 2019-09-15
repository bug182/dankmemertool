import os

test = os.system('py -m pip') 
print(test)
os.system('cls')

if test == 0:
    os.system('py -m pip install --upgrade pip')
    os.system('py -m pip install selenium')
else:
    os.system('python -m pip install --upgrade pip')
    os.system('python -m pip install selenium')