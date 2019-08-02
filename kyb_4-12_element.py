from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['platformVersion'] = '5.1.1'

desired_caps['app'] = r'C:\Users\honkly\kaoyan3.1.0.apk'
desired_caps['appPackage'] = 'com.tal.kaoyan'
desired_caps['appActivity'] = 'com.tal.kaoyan.ui.activity.SplashActivity'

# desired_caps['noReset'] = 'False'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)

# driver.find_element_by_id('android:id/button2').click()
# driver.find_element_by_id('com.tal.kaoyan:id/tv_skip').click()

def check_cancelBton():
    print("Check Cancel Button")

    try:
        cancelBtn = driver.find_element_by_id('android:id/button2')
    except NoSuchElementException:
        print("No Cancel Button")
    else:
        cancelBtn.click()

def check_skipBtn():
    print("Check skip button")

    try:
        skipBtn = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except:
        print("No skip button")
    else:
        skipBtn.click()

check_cancelBton()
check_skipBtn()