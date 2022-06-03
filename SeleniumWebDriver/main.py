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
    driver = webdriver.Chrome()

    driver.get("http://prom-ecosystem-ruk-8340-dev.apps.ocpd.sib.evraz.com/general")

    driver.implicitly_wait(4)

    #search_box = driver.find_element(by=By.NAME, value="q")
    # search_box = driver.find_element(by=By.NAME, value="q")
    # search_button = driver.find_element(by=By.NAME, value="btnK")
    print("search")
    #search_div = driver.find_element(by=By.CLASS_NAME, value="Распадская 7 пласт")
    search_box = driver.find_elements_by_xpath("//*[contains(text(), 'Распадская 7 пласт')]")
    assert search_box
    #search_box[0].click()
    driver.implicitly_wait(4)

    # search_box.send_keys("Selenium")
    # search_button.click()
    #
    # search_box = driver.find_element(by=By.NAME, value="q")
    # value = search_box.get_attribute("value")
    # assert value == "Selenium"

    driver.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
