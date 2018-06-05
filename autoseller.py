# Created by Kwacate
# V 1.0
# Bitploy?
#
###    Import the Stuff ###

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
import time


###     Initial variables and list holders ###

random_time_sleep = randint(5, 20)
groups = []
sell_list = []

f_lista = "lista.txt"
f_grupos = "grupos.txt"


###     Loading data from files ### 

    # Loading gropus into list
groups_list = open(f_grupos, 'r', encoding="utf-8")

for line in groups_list.readlines():
    groups.append(line.strip())
print (len(groups), "Listed groups Loaded!")


    # Loading sell_list Items
Lista = open('lista.txt', 'r', encoding="utf-8")
list_items = []
for line in Lista.readlines():
    list_items.append(line.strip())
    sell_list.append(line.strip())
print (len(list_items), "Items to sell Loaded!")





###     Opening and handling Web Browser ###

    # opening web.Whatsapp 
web = webdriver.Firefox()
web.get('http://web.whatsapp.com')

    # Scanning the QR Code
input('Enter anything after scanning QR code')
time.sleep(5)

# Finding Groups
for name in groups:
    user = web.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    msg_box = web.find_element_by_class_name('_2S1VP')
    # sending messages
    for line in sell_list:
        msg_box.send_keys(line)
        ActionChains(web).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).perform()


    button = web.find_element_by_class_name('_2lkdt')
    button.click()
    # Sleep random time
    time.sleep(random_time_sleep)




###     check

print ("The following groups had been message:")
print (groups)
print ("Message Sent:")
print (sell_list)
input ("Hit enter/return or enter any key to quit")