from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
import time
driver = webdriver.Chrome()
driver.get("link-to-web")

optionsList = []

def enter_payslip_menu():
    driver.switch_to.default_content()
    driver.switch_to_frame("frmmenu")
    driver.find_element_by_link_text('Payslip').click()
    driver.switch_to.default_content()
    driver.switch_to_frame("content")       

def retrieve_list():
    optionsList = []
    select = driver.find_element_by_xpath( "//select[@name='externalPayslipOid']")
    options = select.find_elements_by_tag_name("option")    
    for option in options: 
        optionsList.append(option.get_attribute("value"))
    return optionsList
    
def download_payslips():
    x = retrieve_list()    
    for i in range(len(x)):
        months_list = retrieve_list()        
        select = Select(driver.find_element_by_xpath( "//select[@name='externalPayslipOid']"))
        select.select_by_value(months_list[i])
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/form/table[2]/tbody/tr[2]/td[3]/input").click()    
        time.sleep(1)        
        alert_obj = driver.switch_to.alert
        alert_obj.accept()
        time.sleep(10)                
        driver.switch_to.default_content()
        driver.switch_to_frame("frmmenu")
        driver.find_element_by_link_text('Payslip').click()
        driver.switch_to.default_content()
        driver.switch_to_frame("content")
        time.sleep(2)