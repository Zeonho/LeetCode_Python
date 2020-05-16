from selenium.webdriver import Chrome 
from selenium.common.exceptions import WebDriverException
from bs4 import BeautifulSoup
import sys
import os
import re
import time



class Question_Parser:
    def __init__(self):
        self.driver = Chrome()
        
        # Login
        self.login_option = False
        self.login_url = 'https://leetcode.com/accounts/login/'
        self.login_account_file = ""

        # Problem
        # self.problem_url = sys.argv[1]
        # if not self.problem_url:
        #     self.problem_url = input()

        # self.driver.get(self.problem_url)
        self.get_problem_url(sys.argv[1])

        # title is obtained by get_title function
        self.title = ""
        # title is obtained by get_question_description function
        self.problem = ""
        # title is obtained by get_starter_code function
        self.starter_code =""

    def get_problem_url(self, number):
        problem_serach_url = "https://leetcode.com/problemset/all/?search="
        problem_serach =  problem_serach_url + number
        self.driver.get(problem_serach)
        time.sleep(2)
        a_href = self.driver.find_element_by_xpath("//table/tbody[1]/tr/td[3]/div/a")
        time.sleep(0.5)
        a_href.click()

    def login(self):

        with open(login_account_file) as f:
            USERNAME = f.readline()
            PASSWORD = f.readline()


        if USERNAME and PASSWORD:
            self.driver.get(self.login_url)
            
            username_field = self.driver.find_elements_by_class_name("input__2W4f")[0]
            password_field = self.driver.find_elements_by_class_name("input__2W4f ")[1]
            username_field.send_keys(USERNAME)
            password_field.send_keys(PASSWORD)

            signin = self.driver.find_element_by_class_name("btn-content__lOBM")
            flag = True

            while(flag):
                try:
                    time.sleep(0.5)
                    signin.click()
                    flag = False
                except WebDriverException:
                    time.sleep(0.5)
            time.sleep(1)
            if(self.driver.current_url != self.login_url):
                print('Login succeeded')
                return True
            else:
                print('Login failed - check username and password')
                return False
        print('Need to provide a username and password!')
        return False

    def stupid_leetcodeCN_handler(self):
        # Stupid Leetcode CN 
        time.sleep(3)
        self.driver.get(self.driver.current_url.replace("leetcode-cn","leetcode"))
        while "leetcode-cn" in self.driver.current_url:
            time.sleep(2)
    
    def get_title(self):

        success = False
        try_times = 0

        while not success:
            try_times += 1
            try:
                self.title = self.driver.find_element_by_class_name("css-v3d350").text
                success = True
            except WebDriverException:
                time.sleep(0.5)

            if try_times == 5:
                self.driver.get(self.problem_url)

                
            elif try_times > 10:
                print("Parsing title fail")
                return False

        return success


    def get_question_description(self):

        success = False
        try_times = 0
        doc_mark = '"""'
        new_line_mark = "\n"

        while not success:
            try_times += 1
            try:
                content = self.driver.find_element_by_class_name("question-content__JfgR").text
                success = True
            except WebDriverException:
                time.sleep(0.5)
            
            if try_times > 10:
                print("Parsing question content fail")
                return False
                

            

        self.problem = doc_mark + new_line_mark + content + new_line_mark  + doc_mark + new_line_mark
        return success

    def get_starter_code(self):


        success = False
        try_times = 0
        doc_mark = '"""'
        new_line_mark = "\n"

        while not success:
            try_times += 1
            try:
                # Obtain starter code
                language_dropdown = '//*[@id="app"]/div/div[3]/div/div/div[3]/div/div[1]/div/div[1]/div[1]/div'
                select_arrow = self.driver.find_element_by_class_name('ant-select-arrow')
                time.sleep(1)
                python3_option = '/html/body/div[7]/div/div/div/ul/li[4]'
                select_arrow.click()
                self.driver.find_element_by_xpath(python3_option).click()
                time.sleep(1)
                success = True    
            except WebDriverException:
                time.sleep(0.5)
                

            if try_times > 10:
                print("Parsing starter code  fail")
                return False

        self.starter_code = ""
        for line in self.driver.find_elements_by_class_name("CodeMirror-line"):
            self.starter_code += line.text + "\n"

        return success
        

        



    def create_file(self):
        try:
            if self.get_title():
                f_name = self.title
                f_name = f_name.replace('.', '')
                f_name = f_name.replace(' ', '_')
                f_name += ".py"
                f = open(f_name, "w")

            
            if self.get_question_description() and self.get_starter_code():
                f.write(self.problem + "\n"+ self.starter_code)


            print(f_name, " Created")
        except IOError as e:
            print (e)
        finally:
            f.close()
            self.driver.close()


    def run(self):
        self.create_file()
            

if __name__ == "__main__":
    pp = Question_Parser()
    pp.run()

    