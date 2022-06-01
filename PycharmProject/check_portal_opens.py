from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # service = Service(executable_path=ChromeDriverManager().install())
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # driver = webdriver.Chrome()
    # driver.get("https://google.com")
    # title = driver.title
    # print(title)
    # driver = webdriver.Chrome()
    #
    # driver.get("http://prom-ecosystem-ruk-8340-dev.apps.ocpd.sib.evraz.com/general")
    #
    # driver.implicitly_wait(4)
    #
    # #search_box = driver.find_element(by=By.NAME, value="q")
    # # search_box = driver.find_element(by=By.NAME, value="q")
    # # search_button = driver.find_element(by=By.NAME, value="btnK")
    # print("search")
    # #search_div = driver.find_element(by=By.CLASS_NAME, value="Распадская 7 пласт")
    # search_box = driver.find_elements_by_xpath("//*[contains(text(), 'Распадская 7 пласт')]")
    # assert search_box
    # #search_box[0].click()
    # driver.implicitly_wait(4)

    # search_box.send_keys("Selenium")
    # search_button.click()
    #
    # search_box = driver.find_element(by=By.NAME, value="q")
    # value = search_box.get_attribute("value")
    # assert value == "Selenium"

    driver = webdriver.Chrome()

    driver.get("http://prom-ecosystem-ruk-8340-dev.apps.ocpd.sib.evraz.com/sinking/workings?mine_id=1&lava_id=1&sector_id=0&actual=true&operationalPlan=true&period_type=year")
    driver.implicitly_wait(4)

    count = len(driver.find_elements(By.XPATH,".//*[contains(@class, \'recharts-text recharts-label\')and contains(@text-anchor, \'start\')]//*"))
    sum = 0

    print(f"Количество нодов: {count}")
    while count > 0:
        element = driver.find_element(By.XPATH,
                                           f".//*[contains(@class, \'recharts-text recharts-label\')and contains(@text-anchor, \'start\')][{count}]//*").text
        print(f"Элемент: {element}")
        sum += int(element)
        count -= 1

    print(f"Получившиеся сумма {sum}")
    plan = int(driver.find_element(By.XPATH, ".//span[@data-tip=\'Прогнозное значение на 2022 год\']").text)
    assert (sum == plan)

    driver.quit()



if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
