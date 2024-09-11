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

        self.USA: WebElement = self.TABLE.find_element(By.XPATH, "//tr[contains(., 'U.S.')]")
        self.BRAZIL: WebElement = self.TABLE.find_element(By.XPATH, "//tr[contains(., 'Brazilian')]")
        self.UKRAINE: WebElement = self.TABLE.find_element(By.XPATH, "//tr[contains(., 'Ukrainian')]")
        self.CHINA: WebElement = self.TABLE.find_element(By.XPATH, "//tr[contains(., 'Chinese')]")
        self.TAIWAN: WebElement = self.TABLE.find_element(By.XPATH, "//tr[contains(., 'Taiwan')]")
        self.PHILLIPINES: WebElement = self.TABLE.find_element(By.XPATH, "//tr[contains(., 'Philippine')]")
        self.RUSSIA: WebElement = self.TABLE.find_element(By.XPATH, "//tr[contains(., 'Russian')]")
        
        self.COUNTRIES: list[WebElement] = [self.USA, self.BRAZIL, self.UKRAINE, self.CHINA, self.TAIWAN, self.PHILLIPINES, self.RUSSIA]
        
        for _, country in enumerate(self.COUNTRIES):
            self.CONVERTED_PRICE = country.find_element(By.CLASS_NAME, "table-prices-converted")
            self.COUNTRY_NAME = country.find_element(By.CLASS_NAME, "price-line").text

            print(Fore.GREEN + self.COUNTRY_NAME + " : " + Fore.LIGHTCYAN_EX + self.CONVERTED_PRICE.text)

if __name__ == "__main__":
    SCRAPER: scraper = scraper()

