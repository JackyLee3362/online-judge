from selenium import webdriver
import time

url = "https://m.tb.cn/h.fHzcryw?tk=pWTV297RO5K"
browser = webdriver.Edge()
browser.get(url)
time.sleep(8)
print('hello')
# signin_link = browser.find_element_by_link_text("登录")
button = driver_wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'h')))
button.click()
username_sender = driver_wait.until(EC.presence_of_element_located((By.ID, 'fm-login-id')))
username_sender.send_keys(username)
password_sender = driver_wait.until(EC.presence_of_element_located((By.ID, 'fm-login-password')))
password_sender.send_keys(password)
# signin_link.click()