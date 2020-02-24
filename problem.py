from selenium.webdriver import Chrome 
from selenium.common.exceptions import WebDriverException
from bs4 import BeautifulSoup
import sys
import os
import re
import time
driver = Chrome()
driver.implicitly_wait(20)

def login(name='', pwd=''):
    login_url = 'https://leetcode.com/accounts/login/'

    if name and pwd:
        driver.get(login_url)
        # driver.implicitly_wait(20)
        user = driver.find_elements_by_class_name("input__2W4f")[0]
        pwd = driver.find_elements_by_class_name("input__2W4f ")[1]
        user.send_keys(USERNAME)
        pwd.send_keys(PASSWORD)

        signin = driver.find_element_by_class_name("btn-content__lOBM")
        flag = True
        #TODO: make this less ugly - we need to wait for the page to 
        #fully load before login can be clicked
        while(flag):
            try:
                time.sleep(0.5)
                signin.click()
                flag = False
            except WebDriverException:
                time.sleep(0.5)
        time.sleep(1)
        if(driver.current_url != login_url):
            print('Login succeeded')
            return True
        else:
            print('Login failed - check username and password')
            return False
    print('Need to provide a username and password!')
    return False

# with open(".account") as f:
#     USERNAME = f.readline()
#     PASSWORD = f.readline()

# login(USERNAME, PASSWORD)
problem_url = sys.argv[1]
if not problem_url:
    problem_url = input()
driver.get(problem_url)


time.sleep(3)
driver.get(driver.current_url.replace("leetcode-cn","leetcode"))
while "leetcode-cn" in driver.current_url:
    time.sleep(3)



title = driver.find_element_by_class_name("css-v3d350").text
if title:
    try:
        f_name = title
        f_name = f_name.replace('.', '')
        f_name = f_name.replace(' ', '_')
        f_name += ".py"
        f = open(f_name, "w")

        doc_mark = '"""'
        new_line_mark = "\n"


        content = driver.find_element_by_class_name("question-content__JfgR").text
        problem = doc_mark + new_line_mark + content + new_line_mark  + doc_mark + new_line_mark

        

        # Obtain starter code
        language_dropdown = '//*[@id="app"]/div/div[3]/div/div/div[3]/div/div[1]/div/div[1]/div[1]/div'
        time.sleep(1)
        python3_option = '/html/body/div[7]/div/div/div/ul/li[4]'
        driver.find_element_by_xpath(language_dropdown).click()
        driver.find_element_by_xpath(python3_option).click()
        time.sleep(1)

        starter_code = ""
        for line in driver.find_elements_by_class_name("CodeMirror-line"):
            starter_code += line.text + "\n"


        f.write(problem + "\n"+ starter_code)
        print(f_name, " Created")
    except IOError as e:
        print (e)
    finally:
        f.close()
        driver.close()

