# !/usr/bin/env python -*- coding: utf-8 -*-

import os
import sys
import time
import random
from selenium import webdriver
from playsound import playsound
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

######################################################1
#Init Browser


def searcher(sword):

    search_input = browser.find_element(By.XPATH,'/html/body/div/div[2]/div[3]/div[1]/dic/div[2]/div[1]/div/form/div/input')

    print("Clear Search Box")
    for element in range(0, len(sword) + 4):
        search_input.send_keys(Keys.BACK_SPACE)
        time.sleep(0.5)

    print(sword + " Typed")
    search_input.send_keys(sword)

    time.sleep(4)

    print("Pressing Enter")
    search_input.send_keys(Keys.RETURN)
    
    time.sleep(4)


acFile = open("Accounts.txt", "r")

accountFile = acFile.readlines()

lastAccount = open("LastAccount.txt", "r+")

lastAccountNumber = int(lastAccount.readline())

accountNumberFile = open("AccountNumber.txt", "r")

accountNumber = int(accountNumberFile.readline())

accountNumberFile.close()

for s in range(lastAccountNumber, accountNumber) :

    startTime = time.time()    

    options = Options()

    options.add_argument("--width=800");

    options.add_argument("--height=640");

    options.set_preference('profile', 'C:\\Users\\Admin\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\x2gpmyrg.default-release')

    service = Service('C:\\geco\\geckodriver')

    browser = webdriver.Firefox(options=options, service=service)

    referralFile = open("Referral.txt", "r")

    referral = referralFile.readline()

    browser.get(referral)

    referralFile.close()

    joinBtn = browser.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[1]/div[2]/div/a')

    joinBtn.click()

    time.sleep(4)

    email = browser.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div[3]/div[2]/form/div[1]/input')

    password = browser.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div[3]/div[2]/form/div[2]/input')

    confirmPassword = browser.find_element(By.XPATH,'//*[@id="password-confirm"]')

    email.send_keys(accountFile[lastAccountNumber*3])

    password.send_keys(accountFile[(lastAccountNumber*3) + 1])

    confirmPassword.send_keys(accountFile[(lastAccountNumber*3) + 1])

    playsound('audio.mp3')

    time.sleep(3)

    lastAccountNumber = lastAccountNumber + 1

    time.sleep(40)

    print("Sleep Over")
    try:
        skipTour = browser.find_element(By.XPATH,'/html/body/div[5]/div/div[5]/a[1]')
    except:
        sys.exit()

# Saving Last Regester Account
    lastAccount.seek(0, os.SEEK_SET)
    lastAccount.write(str(lastAccountNumber))

    skipTour.click()

    time.sleep(1)

    browser.switch_to.alert.accept()

    time.sleep(1)
    
    firstSearch = browser.find_element(By.XPATH,'//*[@id="search"]')

    firstSearch.send_keys('Pre')
    print("firstSearch")

    time.sleep(1)
    print("Pre Typed")

    firstSearch.send_keys(Keys.RETURN)
    print("Pressing Enter")
    
    time.sleep(7)

    loginBtn = browser.find_element(By.XPATH,'/html/body/div/div[2]/div[3]/div[1]/dic/div[2]/div[3]/div[1]/div[5]/div/div[2]/div')

    loginBtn.click()

    time.sleep(3)

    with open("NewSearch.txt", "r") as file:
        allWords = file.read()
        words = list(map(str, allWords.split()))
    
    
    wordNumberFile = open("WordNumber.txt", "r")

    wordNumber = int(wordNumberFile.readline())

    wordNumberFile.close()

    for kounter in range(1, wordNumber + 1):
        sword = random.choice(words)
        searcher(sword)
            
        precoins = browser.find_element(By.XPATH,'/html/body/div/div[2]/div[3]/div[1]/dic/div[2]/div[3]/div[1]/div[5]/div/div[2]/a[1]')

        print(" ")

        if kounter == 1 :
            firstPrecoins = round(float(precoins.text[0:6]), 4)

        print("Your Balance After " + str(kounter) + " Search In This Session : " + precoins.text)

        print(" ")
        earnedCoins = round(float(precoins.text[0:6]) - firstPrecoins, 4)
        print("You Earn " + str(earnedCoins) + " Token, So Far, For This Session")
        print(" ")

    earnedCoins = round(float(precoins.text[0:6]) - firstPrecoins, 4)
    file.close()
    browser.close()
    print("Closing Browser For Next Account \n")
    print("You Earn " + str(earnedCoins) + " From This Account : " + accountFile[(lastAccountNumber - 1)*3])
    print("^^^^^^^^^^^ Account Number ^^^^^^^^^^^ -> "+ str(lastAccountNumber - 1) +" <- ^^^^^^^^^^^ Account Number ^^^^^^^^^^^")
    endTime = time.time()
    print(" ")
    print("Process Time For This Account -->> : %s" % (endTime - startTime) + " Seconds")
    print(" ")


acFile.close()
    
lastAccount.close()
input()