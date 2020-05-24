from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')

htmlElem = browser.find_element_by_tag_name('html')

while True:
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.LEFT)
    try:
        gameOverElem = browser.find_element_by_class_name('game-message game-over')
        break
    except:
        continue
