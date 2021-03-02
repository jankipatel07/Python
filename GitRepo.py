from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager
import getpass

USERNAME = input('Enter github username: ')
PASSWORD = getpass.getpass('Enter password: ')


url = 'https://www.github.com'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

wait = WebDriverWait(driver, 10)
# launchEarthBtn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/header/div/nav[1]/ul[2]/li[2]/a/span/span')))
# launchEarthBtn.click()

# signup = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/header/div/div[2]/div[2]/a[1]')))
# signup.click()

signin = driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]')
signin.click()

usr_name = driver.find_element_by_xpath('//*[@id="login_field"]')
usr_name.send_keys(USERNAME)
password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys(PASSWORD)
login_btn = driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/input[14]')
login_btn.click()
repo_click = driver.find_element_by_xpath('//*[@id="repos-container"]/h2/a')
repo_click.click()
repo_name = driver.find_element_by_xpath('//*[@id="repository_name"]')
repo_name.send_keys('repo_from_selenium')
readme = driver.find_element_by_xpath('//*[@id="repository_auto_init"]')
readme.click()
create_repo_btn = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="new_repository"]/div[4]/button')))
create_repo_btn.click()
