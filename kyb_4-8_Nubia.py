from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'NX507J'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['udid'] = '5f91c1f1'

desired_caps['app'] = r'C:\Users\honkly\com.tal.kaoyan.apk'
desired_caps['appPackage'] = 'com.tal.kaoyan'
desired_caps['appActivity'] = 'com.tal.kaoyan.ui.activity.SplashActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)