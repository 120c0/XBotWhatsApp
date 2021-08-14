from typing import KeysView
import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


from simon.chat.pages import ChatPage
from simon.chats.pages import PanePage

LOG_PERMISSION = True

def log(message):
  if LOG_PERMISSION:
    print(message)

class WebDriver():
  def __init__(self, executable_path : str = '/usr/bin/chromedriver', open_now : bool = True) -> None:
    self.__executable_path = executable_path
    
    self.__options = webdriver.ChromeOptions()
    self.__options.add_argument('--user-data-dir=./User_Data')

    self.driver = webdriver.Chrome(executable_path=self.__executable_path, options=self.__options)
    if open_now:
      self.open_browser()

  def open_browser(self) -> None:
    log(f'Opening chrome driver from {self.__executable_path}')
    self.driver.get('https://web.whatsapp.com')

  def find_element_by_class(self, class_name) -> object:
    return WebDriverWait(self.driver, 10).until(
      expected_conditions.presence_of_element_located((By.CLASS_NAME, class_name))
    )

  def get_last_message(self):
    data = self.get_messages_div()
    data = data[len(data) - 1].find_elements_by_xpath('//span[@class="i0jNr selectable-text copyable-text"]')
    return str(data[len(data) - 1].text)

  def get_messages_div(self) -> object:
    return self.driver.find_elements_by_xpath("//div[@class='_22Msk']") 

  def close(self) -> None:
    self.driver.close()

  def write_on_input(self, message, class_name) -> None:
    self.input = self.find_element_by_class(class_name)
    self.input.click()
    
    self.input.send_keys(message.replace('\n','') + Keys.ENTER)