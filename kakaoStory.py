import io
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("c:/chromedriver")
rootPath = 'c:/img'
def scroll():
    for i in range(10):
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
        time.sleep(0.3)

def getUrl(dir):
    driver.get(dir)

def getElement(css_selector):
    return driver.find_element(By.CSS_SELECTOR, css_selector)

def getElement2(cusDriver, css_selector):
    return cusDriver.find_element(By.CSS_SELECTOR, css_selector)

def getElements(css_selector):
    return driver.find_elements(By.CSS_SELECTOR, css_selector)

def getElements2(cusDriver, css_selector):
    return cusDriver.find_elements(By.CSS_SELECTOR, css_selector)

def sendKey(css_selector, val):
    driver.find_element(By.CSS_SELECTOR, css_selector).send_keys(val)

def sendKey2(cusDriver, css_selector, val):
    cusDriver.find_element(By.CSS_SELECTOR, css_selector).send_keys(val)

def click(css_selector) :
    driver.find_element(By.CSS_SELECTOR, css_selector).click()

def click2(cusDriver, css_selector) :
    cusDriver.find_element(By.CSS_SELECTOR, css_selector).click()

def kakaoLogin():
    getUrl('https://accounts.kakao.com/login/kakaostory')
    sendKey('input#loginEmail', 'bangae2@gmail.com')
    sendKey('input#loginPw', 'fpdlwms1@')
    time.sleep(2)
    click('button.btn_login')
    time.sleep(2)

def kakaoLogin2(cusDriver):
    cusDriver.get('https://accounts.kakao.com/login/kakaostory')
    sendKey2(cusDriver,'input#loginEmail', 'bangae2@gmail.com')
    sendKey2(cusDriver,'input#loginPw', 'fpdlwms1@')
    time.sleep(2)
    click2(cusDriver, 'button.btn_login')
    time.sleep(2)

def mkdir(dir) :
    try:
        os.mkdir(rootPath)
    except Exception :
        print()
    path = os.path.join(rootPath, dir)
    try:
        os.mkdir(path)
    except Exception :
        print()
    return path




def subMain():
    wrappers = getElements('div._wrapper')
    height = 0
    driver.execute_script("window.scrollBy(0, "+str(height)+")")
    wrapCnt = 1
    for wrapper in wrappers :
        sections = getElements2(wrapper, 'div.section')
        print(len(sections))
        for section in sections :

            print(section.get_attribute("innerHTML"))
            titleDiv = getElement2(section, 'div._content')
            header = titleDiv.get_attribute("innerHTML")
            title = header.split('<br>')[0]
            tit = title.split(' ')[0]
            path = mkdir(tit)
            # print(titles[0].split(' ')[0])
            img_wrap = getElement2(section, 'div.img_wrap')
            imgs = getElements2(img_wrap, 'img')
            imgCnt = 1
            for img in imgs:
                src = img.get_attribute("src")
                driver.execute_script('''window.open("about:blank", "_blank");''')
                driver.switch_to_window(driver.window_handles[1])
                driver.get(src)
                element = driver.find_element(By.CSS_SELECTOR, 'img')
                location = element.location
                size = element.size
                png = driver.get_screenshot_as_png()  # saves screenshot of entire page
                im = Image.open(BytesIO(png))  # uses PIL library to open image in memory
                left = location['x']
                top = location['y']
                right = location['x'] + size['width']
                bottom = location['y'] + size['height']
                driver.execute_script('self.close()')
                imgCnt = imgCnt + 1
                driver.switch_to_window(driver.window_handles[0])
        wrapCnt = wrapCnt + 1
def main():
    kakaoLogin()
    getUrl('https://story.kakao.com/bestnini')
    time.sleep(2)
    scroll()
    subMain()


main()
