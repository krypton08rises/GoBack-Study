import os
import sys
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False
binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox')
driver = webdriver.Firefox(capabilities=cap, firefox_binary=binary)

def check_tabs():
    print(driver.current_url)


r = []
r = os.popen('tasklist /v').read().strip().split('\n')
for url in r:
    if "firefox.exe" in url:
        check_tabs()
sys.exit(0)
