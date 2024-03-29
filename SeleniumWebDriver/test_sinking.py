# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSinking():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_raspadskaya7prohodka(self):
    self.driver.get("http://prom-ecosystem-ruk-8340-dev.apps.ocpd.sib.evraz.com/sinking/workings?mine_id=1&lava_id=1&sector_id=0&actual=true&operationalPlan=true&period_type=year")
    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//span[@data-tip=\'Прогнозное значение на 2022 год\']")))
    self.vars["plan"] = self.driver.find_element(By.XPATH, ".//span[@data-tip=\'Прогнозное значение на 2022 год\']").text
    print("Значение плана: {}".format(self.vars["plan"]))
    self.vars["budget"] = self.driver.find_element(By.XPATH, ".//span[@data-tip=\'Значение планa на 2022 год\']").text
    print("Значение бюджета: {}".format(self.vars["budget"]))
    assert(self.vars["plan"] == 'self.vars["budget"]')
  
  def test_raspadskaya7checkplan(self):
    self.driver.get("http://prom-ecosystem-ruk-8340-dev.apps.ocpd.sib.evraz.com/sinking/workings?mine_id=1&lava_id=1&sector_id=0&actual=true&operationalPlan=true&period_type=year")
    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//span[@data-tip=\'Прогнозное значение на 2022 год\']")))
    count = len(self.driver.find_elements(By.XPATH, ".//*[contains(@class, \'recharts-text recharts-label\')and contains(@text-anchor, \'start\')]//*"))
    sum = 0
    #self.vars["count"] = len(self.driver.find_elements(By.XPATH, ".//*[contains(@class, \'recharts-text recharts-label\')and contains(@text-anchor, \'start\')]//*"))
    #self.vars["sum"] = "0"
    print(f"Количество нодов: {count}")
    while count > 0:
      element = self.driver.find_element(By.XPATH, f".//*[contains(@class, \'recharts-text recharts-label\')and contains(@text-anchor, \'start\')][{count}]//*").text
      print(f"Элемент: {element}")
      sum += int(element)
      count -= 1

    print(f"Получившиеся сумма {sum}")
    plan = int(self.driver.find_element(By.XPATH, ".//span[@data-tip=\'Прогнозное значение на 2022 год\']").text)
    assert(sum == plan)
  
