from capability import driver
import random

driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_userheader').click()

images = driver.find_elements_by_id('com.tal.kaoyan:id/item_image')
images[2].click()
driver.find_element_by_id('com.tal.kaoyan:id/save').click()

username = 'honk2019' + str(random.randint(1000, 9000))
print(username)
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_username_edittext').send_keys(username)

password = 'elon2019' + str(random.randint(1000, 9000))
print(password)
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_password_edittext').send_keys(password)

email = 'elon' + str(random.randint(1000, 90000)) + '@163.com'
print(email)
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_email_edittext').send_keys(email)
# 点击注册按钮
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_register_btn').click()

# 院校选择
driver.find_element_by_id('com.tal.kaoyan:id/perfectinfomation_edit_school_name').click()
driver.find_elements_by_id('com.tal.kaoyan:id/more_forum_title')[1].click()
driver.find_elements_by_id('com.tal.kaoyan:id/university_search_item_name')[1].click()

# 专业选择
driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_major').click()
driver.find_elements_by_id('com.tal.kaoyan:id/major_subject_title')[7].click()
driver.find_elements_by_id('com.tal.kaoyan:id/major_group_title')[8].click()
driver.find_elements_by_id('com.tal.kaoyan:id/major_search_item_name')[0].click()

# 点击进入考研帮
driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_goBtn').click()

# 点击“我知道了”
driver.find_element_by_id('com.tal.kaoyan:id/task_no_task').click()