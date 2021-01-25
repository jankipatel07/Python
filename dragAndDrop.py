from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')

source = driver.find_element_by_xpath('//*[@id="box3"]')
des = driver.find_element_by_xpath('//*[@id="box103"]')

actions = ActionChains(driver)
actions.drag_and_drop(source, des).perform()