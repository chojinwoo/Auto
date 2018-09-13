import os
import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
import glob

rootPath = 'c:/img/'
def newChrome() :
    return webdriver.Chrome("d:/chromedriver")

def connectUrl(driver, url) :
    driver.get(url)

def clickEvent(driver, css_selector):
    driver.find_element(By.CSS_SELECTOR, css_selector).click()

def sendKey(driver, css_selector, value):
    driver.find_element(By.CSS_SELECTOR, css_selector).send_keys(value)

def main():
    driver = newChrome()
    connectUrl(driver, "https://www.smartpost.kr/")
    clickEvent(driver , 'button[data-target="#login-modal"')
    time.sleep(1)
    sendKey(driver, '#LoginID', 'bangae1')
    sendKey(driver, '#LoginPW', 'fpdlwmS12@')
    clickEvent(driver, 'div.form-section>div.ntm-table-cell>button')
    clickEvent(driver, '#closeNotice')

    folders = glob.glob(rootPath + '*')
    for folder in folders:
        filenames = ''
        files = glob.glob(folder + "/*.png")
        lastIdx = len(files)
        if lastIdx > 9:
            lastIdx = 9

        for i in range(lastIdx) :
            sendKey(driver, '#inpAddFile', files[i])

        f = open(folder + "/detail.txt", mode='r', encoding='utf-8')
        str = ''
        while True:
            line = f.readline()
            if not line : break
            print(line)
            str = str + line + '\r\n'
        f.close()
        sendKey(driver, 'div.emojionearea-editor', str)
        time.sleep(100)
main()
