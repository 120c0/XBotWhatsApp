from logging import currentframe
from typing_extensions import final
import selenium
from selenium import webdriver
from WebDriver import *
from time import sleep
from Commands import *

into_bot = """
  Robot Test Number 01
"""

class XBot():
  def __init__(self, name):
    self.__name = name
    self.webdriver = WebDriver()
    self.last_message = ""
    self.current_message = ""
  def run(self):
    input("Where is done, press 'Enter': ")

    while True:
      if self.current_message != self.last_message:
        if(commands(self.current_message) != " "):
          self.webdriver.write_on_input(commands(self.current_message), 'p3_M1')

        self.last_message = self.current_message
      else:
        self.current_message = self.webdriver.get_last_message()