
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from Constants import globalConstants,environmentConstants

class TestInvalidlogin():
  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.driver.get(globalConstants.BASEURL)
    self.driver.maximize_window()

  def teardown_method(self):
    self.driver.quit()

  def waitForElenmentVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
  
  def test_invalidlogin(self):
        
    self.waitForElenmentVisible((By.CSS_SELECTOR, environmentConstants.USERNAME))
    username = self.driver.find_element(By.CSS_SELECTOR, environmentConstants.USERNAME)
    username.send_keys("1")
    self.waitForElenmentVisible((By.CSS_SELECTOR, environmentConstants.PASSWORD))
    password = self.driver.find_element(By.CSS_SELECTOR, environmentConstants.PASSWORD)
    password.send_keys("1")
    self.waitForElenmentVisible((By.CSS_SELECTOR, environmentConstants.LOGİN_BTN))
    login = self.driver.find_element(By.CSS_SELECTOR, environmentConstants.LOGİN_BTN)
    login.click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".error-message-container").text == "Epic sadface: Username and password do not match any user in this service"
  
