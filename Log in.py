from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://smartbuzz.angelbroking.com/")
driver.find_element_by_xpath("//a[contains(text(),'Login / Register')]").click()
driver.find_element_by_xpath("//body/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/input[1]").send_keys("sudipta@scaledesk.xyz")
driver.find_element_by_xpath("//input[@id='login-password']").send_keys("123456789")
