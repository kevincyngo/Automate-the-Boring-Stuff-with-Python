from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')

htmlElem = browser.find_element_by_tag_name('html')

while True:
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT)
    try:
        gameOverElem = browser.find_element_by_class_name('game-over')
        score = browser.find_element_by_class_name('score-container').text

        #score string is multi line, we want the first line (the score)
        print("Score: %s" % score.partition('\n')[0])
        browser.quit()
        break
    except:
        continue
