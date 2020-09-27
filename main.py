from itertools import product
from pynput.keyboard import Key, Controller
import multiprocessing
import os
import random
import json
import time
import pyautogui


#Main configuration
save_file = "SAVE.KGN"
mode = 0
platform = "steam"
dictionnary = "AZERTYUIOPQSDFGHJKLMWXCVBN0123456789"
key_length = 15
keygen_count = 100000
######################

steam_waiting_time = 3600

def serialize(lst):
    content = {}
    for key in lst:
        content[key] = 'UNTESTED'
    return content

def save(lst, dbg):
    sv = open(save_file, "w+")
    sv.write(json.dumps(lst))
    sv.close()
    if dbg :
        print("SAVED LINES : " + str(len(lst)))
    return lst

class KEYLIST:
    def __init__(self):
        self.keys = dict()
        self.size = len(self.keys)

#LOAD
if not os.path.exists(save_file):
    sv = open(save_file, "w+")
    sv.write("{}")
    sv.close()

sv = open(save_file, "r")
content = json.loads(sv.read())
sv.close()

key_list = KEYLIST()
key_list.keys = content

def generateRD(key_length, attempt_counter):
    counter = 0
    for _ in range(0,attempt_counter) :
        # bracket_counter = 0
        value = ''
        for x in random.sample(dictionnary,key_length):
            value += x
        #     bracket_counter += 1
        #     if bracket_counter == 5:
        #         value += '-'
        #         bracket_counter = 0
        # if value[len(value)-1] == '-':
        #     value = value[:-1]
        if key_list.keys is None:
            exit()
        if value not in key_list.keys.keys():
            key_list.keys[value] = "UNTESTED"
        counter += 1
        #print('>> KEY : ' + value + " ATTEMPT : " + str(counter) + '/' + str(attempt_counter))
    save(key_list.keys, 1)

# def StartProcesses():
#     p1 = multiprocessing.Process(target=generateRD, args=(key_length,keygen_count))
#     p2 = multiprocessing.Process(target=generateRD, args=(key_length,keygen_count))
#     p3 = multiprocessing.Process(target=generateRD, args=(key_length,keygen_count))
#     p4 = multiprocessing.Process(target=generateRD, args=(key_length,keygen_count))
#     p1.start()
#     time.sleep(0.1)
#     p2.start()
#     time.sleep(0.1)
#     p3.start()
#     time.sleep(0.1)
#     p4.start()

def SteamAutoGUI():
    #Point(x=1026, y=698)
    if str(pyautogui.position()) != "Point(x=1026, y=698)":
        pyautogui.moveTo(1026, 698, 0)
    pyautogui.click()
    time.sleep(1)
    #Point(x=937, y=696)
    if str(pyautogui.position()) != "Point(x=937, y=696)":
        pyautogui.moveTo(937, 696, 0)
    pyautogui.click()
    time.sleep(0.2)
    #Point(x=911, y=511)
    if str(pyautogui.position()) != "Point(x=911, y=511)":
        pyautogui.moveTo(911, 511, 0)
    pyautogui.click()
    pyautogui.click()

keyboard = Controller()
if __name__ == '__main__':
    generateRD(key_length,keygen_count)
    for k,v in key_list.keys.items():
        if v == "UNTESTED":
            if str(pyautogui.position()) != "Point(x=911, y=511)":
                pyautogui.moveTo(911, 511, 0)
            pyautogui.click()
            for char in k:
                keyboard.press(char)
            if platform == "steam":
                SteamAutoGUI()
            key_list.keys[k] = "TESTED"
            time.sleep(steam_waiting_time)
        save(key_list.keys, 1)
    # if mode == 0:
    #     #StartProcesses()
    #     generateRD(key_length,keygen_count)
    #     if str(pyautogui.position()) != "Point(x=911, y=511)":
    #         pyautogui.moveTo(911, 511, 0)
    #     pyautogui.click()
    #     for k,v in key_list.keys.items():
    #         if v == "UNTESTED":
    #             for char in k:
    #                 keyboard.press(char)
    #             if platform == "steam":
    #                 SteamAutoGUI()
    #             key_list.keys[k] = "TESTED"
    #             time.sleep(steam_waiting_time)
    #     save(key_list.keys, 1)
    # else:
    #     if str(pyautogui.position()) != "Point(x=911, y=511)":
    #         pyautogui.moveTo(911, 511, 0)
    #     pyautogui.click()
    #     for k,v in key_list.keys.items():
    #         if v == "UNTESTED":
    #             for char in k:
    #                 keyboard.press(char)
    #             if platform == "steam":
    #                 SteamAutoGUI()
    #             key_list.keys[k] = "TESTED"
    #             time.sleep(steam_waiting_time)
    #     save(key_list.keys, 1)
    exit()
    