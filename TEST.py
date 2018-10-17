from selenium import webdriver
n = ['1',"2",'3']

for i in range (0,3,1):
 driver = webdriver.Chrome()
 driver.get("https://www.google.com")
#找到輸入框
 element = driver.find_element_by_name("q");
#輸入內容
 element.send_keys("hello world");
#提交表單
 element.submit();
 driver.find_element_by_css_selector('#rso a:nth-child(3)').click()
 driver.close()

for v in n:
 print (v)
	

