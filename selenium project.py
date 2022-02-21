from selenium import webdriver
from selenium.webdriver.common import keys; from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
# /Users/name]/Desktop/Selenium/chromedriver if not in PATH

driver = webdriver.Chrome()
url = 'https://healthscreening.schools.nyc/?type=G'
driver.get(url)
student = driver.find_element_by_xpath('//*[@id="guest_identity_form"]/div[2]/div[1]/div').click()  # student button
first_name = driver.find_element_by_xpath('//*[@id="guest_first_name"]').send_keys('test test') # type first name
last_name = driver.find_element_by_xpath('//*[@id="guest_last_name"]').send_keys('test test')   # type last name
button1 = driver.find_element_by_xpath('//*[@id="other_checked"]').click()  # other button for school (alternative for dropdoown menu)
email = driver.find_element_by_xpath('//*[@id="guest_email"]').send_keys('pythonseleniumtest0@gmail.com')   # type email
school_input = driver.find_element_by_xpath('//*[@id="guest_location"]').send_keys('Benjamin N. Cardozo High School (Q415') # type school
submit = driver.find_element_by_xpath('//*[@id="btnDailyScreeningSubmit"]/button').click()  # enter buttton

mp1 = driver.find_element_by_xpath('/html/body/div[1]/form/div[4]/div[1]/div/div/div[2]/div[2]/div/div[3]/label').click() # covid questions
time.sleep(1)  # wait half a second for next question
mp2 = driver.find_element_by_xpath('/html/body/div[1]/form/div[4]/div[1]/div/div/div[2]/div[4]/div[1]/div/div[2]/label').click() # covid questions
time.sleep(1)  # wait half a second for next question
mp3 = driver.find_element_by_xpath('/html/body/div[1]/form/div[4]/div[1]/div/div/div[2]/div[4]/div[2]/div/div[2]/label').click() # covid questions
time.sleep(1)  # wait half a second for next question
mp4 = driver.find_element_by_xpath('/html/body/div[1]/form/div[4]/div[1]/div/div/div[2]/div[4]/div[3]/div/div[3]/label').click() # covid questions
time.sleep(1)  # wait half a second for next question
# mp1 = driver.find_element_by_xpath('/html/body/div[1]/form/div[4]/div[1]/div/div/div[2]/div[1]/div/div[2]/label').click() # covid questions
# time.sleep(1)  # wait half a second for next question
# mp2 = driver.find_element_by_xpath('/html/body/div[1]/form/div[4]/div[1]/div/div/div[2]/div[2]/div/div[2]/label').click()
# time.sleep(1)  # wait half a second for next question
submit = driver.find_element_by_xpath('/html/body/div[1]/form/div[4]/div[1]/div/div/div[2]/div[5]/div[1]/button').click()
time.sleep(3)   # wait a second to submit
# enter = driver.find_element_by_xpath('/html/body/div[1]/form/div[4]/div[1]/div/div/div[2]/div[4]/div[1]/button').click() #  submit button

driver.quit()



