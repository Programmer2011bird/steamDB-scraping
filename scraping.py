from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from colorama import Fore
import selenium.webdriver
from time import sleep


class scraper:
    def __init__(self) -> None:
        self.DRIVER = selenium.webdriver.Chrome()
        self.URL: str = "https://steamdb.info/app/1985810/"

        self.DRIVER.get(self.URL)
        self.DRIVER.maximize_window()

        sleep(10)
        self.DRIVER.execute_script("window.scrollTo(0, (document.body.scrollHeight - 2900))")
        sleep(5)
        
        self.TABLE: WebElement = self.DRIVER.find_element(By.CLASS_NAME, "table-responsive")
        
        for index in range(1, 11):
            self.COUNTRY = self.TABLE.find_element(By.XPATH, f'//*[@id="prices"]/div[4]/div[1]/table/tbody/tr[{index}]')
            
            self.CONVERTED_PRICE = self.COUNTRY.find_element(By.CLASS_NAME, "table-prices-converted").text
            self.COUNTRY_NAME = self.COUNTRY.find_element(By.CLASS_NAME, "price-line").text
            
            print(Fore.LIGHTYELLOW_EX + f"{index}. " + Fore.LIGHTGREEN_EX + self.COUNTRY_NAME + " : " + Fore.LIGHTCYAN_EX + self.CONVERTED_PRICE)


if __name__ == "__main__":
    SCRAPER: scraper = scraper()

