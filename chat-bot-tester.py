from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://www.messenger.com/t/link-to-chat-conversation")

def test_function_template(sleeptime, keyword):
    
    # Customize this function according to your testing needs.
    # 
    # You can get the XPATH, SELECTOR, ID, NAME, etc. of the elements via a browser,
    # e.g. Ctrl-Shift-I in Chrome.
    #
    # For more info, visit: https://selenium-python.readthedocs.io/
    
    xpath = "Replace me with XPATH value."
    selector = "Replace me with SELECTOR value."
    
    #Locating an element via its XPATH.
    driver.find_element_by_xpath(xpath).click()
    
    #Locating an element via its CSS SELECTOR and typing in text.
    driver.find_element_by_css_selector(selector).send_keys(text)    
    
    #Example of how to press ENTER.
    driver.find_element_by_css_selector(selector).send_keys(Keys.RETURN)
    
    #Click a link with text "Start Over".    
    driver.find_element_by_link_text("Start Over").click()
    
    #TODO: Sleep is a little cheat to wait for the elements to load. Refactor later on.
    time.sleep(sleeptime)
    
def test_sample_flow(sleeptime, text):
    
    selector = "#cch_f1c03c147c28ab8 > div._20bp > div._4_j4 > div._4rv3._7og6 > div > div._7kpk > div > div > div:nth-child(1) > div > div._5rpb > div"
    
    #Type text
    driver.find_element_by_css_selector(selector).send_keys(text)
    time.sleep(sleeptime)
    
    #Press send
    driver.find_element_by_css_selector(selector).send_keys(Keys.RETURN)
    time.sleep(sleeptime)        

def main():

    # The file list. txt contains the list of keywords to be tested, seperated by newlines.
    f = open('keywords.txt', 'r')
    keywords = f.readlines()

    for kw in keywords:
        test_nagtetake(1, kw)