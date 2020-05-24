from selenium import webdriver


browser = webdriver.Firefox()
browser.get('https://inventwithpython.com')

#clicking the page
# try:
#     linkElem = browser.find_element_by_link_text('Read Online for Free')
#     type(linkElem)
#     linkElem.click()
# except:
#     print('Was not able to find an element with that name.')

#filling out and submitting forms
browser.get('https://login.metafilter.com')
userElem = browser.find_element_by_id('user_name)
userElem.send_keys('your_real_username_here')

passwordElem = browser.find_element_by_id('user_pass')
passwordElem.send_keys('your_real_password_here')
passwordElem.submit()
