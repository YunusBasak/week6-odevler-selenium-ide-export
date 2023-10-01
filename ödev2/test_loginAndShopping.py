
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from Constants import globalConstants,environmentConstants

class TestLoginAndShopping():
  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.driver.get(globalConstants.BASEURL)
    self.driver.maximize_window()

  
  def teardown_method(self):
    self.driver.quit()

  def WaitForElementVisible(self,locator,timeout=5):
    WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
  
  def test_loginAndShopping(self):

    self.WaitForElementVisible((By.CSS_SELECTOR, environmentConstants.USERNAME))
    usernameInput = self.driver.find_element(By.CSS_SELECTOR, environmentConstants.USERNAME)
    usernameInput.send_keys("standard_user")
    self.WaitForElementVisible((By.CSS_SELECTOR, environmentConstants.PASSWORD))
    passwordInput = self.driver.find_element(By.CSS_SELECTOR, environmentConstants.PASSWORD)
    passwordInput.send_keys("secret_sauce")
    self.WaitForElementVisible((By.CSS_SELECTOR, environmentConstants.LOGIN_BTN))
    login = self.driver.find_element(By.CSS_SELECTOR, environmentConstants.LOGIN_BTN)
    login.click()
    self.WaitForElementVisible((By.CSS_SELECTOR, environmentConstants.ADDTOCART))
    addToCart=  self.driver.find_element(By.CSS_SELECTOR, environmentConstants.ADDTOCART)
    addToCart.click()
    self.WaitForElementVisible((By.CSS_SELECTOR, environmentConstants.CART))
    cart = self.driver.find_element(By.CSS_SELECTOR, environmentConstants.CART)
    cart.click()
    self.WaitForElementVisible((By.LINK_TEXT, "2"))
    numberOfProducts = self.driver.find_element(By.LINK_TEXT, "2")
    numberOfProducts.click()
    self.WaitForElementVisible((By.CSS_SELECTOR, environmentConstants.CHECKOUT))
    checkout = self.driver.find_element(By.CSS_SELECTOR, environmentConstants.CHECKOUT)
    checkout.click()
    self.WaitForElementVisible((By.CSS_SELECTOR, environmentConstants.FIRSTNAME))
    firstName = self.driver.find_element(By.CSS_SELECTOR, environmentConstants.FIRSTNAME)
    firstName.send_keys("Yunus")
    self.WaitForElementVisible((By.CSS_SELECTOR, environmentConstants.LASTNAME))
    lastName = self.driver.find_element(By.CSS_SELECTOR, environmentConstants.LASTNAME)
    lastName.send_keys("Basak")
    self.WaitForElementVisible((By.CSS_SELECTOR, environmentConstants.POSTALCODE))
    postalCode = self.driver.find_element(By.CSS_SELECTOR, environmentConstants.POSTALCODE)
    postalCode.send_keys("34000")
    self.WaitForElementVisible((By.CSS_SELECTOR,environmentConstants.CONTINUE_BTN))
    continueBtn = self.driver.find_element(By.CSS_SELECTOR, environmentConstants.CONTINUE_BTN)
    continueBtn.click()
    self.WaitForElementVisible((By.CSS_SELECTOR, environmentConstants.FINISH_BTN))
    finishBtn = self.driver.find_element(By.CSS_SELECTOR, environmentConstants.FINISH_BTN)
    finishBtn.click()
    self.WaitForElementVisible((By.CSS_SELECTOR, environmentConstants.HOMEPAGE))
    assert self.driver.find_element(By.CSS_SELECTOR, environmentConstants.HOMEPAGE).text == "Back Home"
    homePage = self.driver.find_element(By.CSS_SELECTOR, environmentConstants.HOMEPAGE)
    homePage.click()

  
