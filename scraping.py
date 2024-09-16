from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import selenium.webdriver
from lxml import etree
from time import sleep
import requests


class game_scraper:
    def __init__(self, Game_Id: str) -> None:
        self.DRIVER = selenium.webdriver.Chrome()
        self.URL: str = f"https://steamdb.info/app/{Game_Id}/"

        self.DRIVER.get(self.URL)
        self.DRIVER.maximize_window()

        sleep(10)
        self.DRIVER.execute_script("window.scrollTo(0, (document.body.scrollHeight - 2900))")
        sleep(5)
    
    def get_info(self) -> list[tuple[str, float]]:
        self.OUTPUT: list[tuple[str, float]] = []
        
        self.TABLE: WebElement = self.DRIVER.find_element(By.CLASS_NAME, "table-responsive")
        
        for index in range(1, 11):
            self.COUNTRY = self.TABLE.find_element(By.XPATH, f'//*[@id="prices"]/div[4]/div[1]/table/tbody/tr[{index}]')
            
            self.CONVERTED_PRICE: str = self.COUNTRY.find_element(By.CLASS_NAME, "table-prices-converted").text
            self.COUNTRY_NAME: str = self.COUNTRY.find_element(By.CLASS_NAME, "price-line").text
            
            self.OUTPUT.append(self.__formatter(self.COUNTRY_NAME, self.CONVERTED_PRICE))

        return self.OUTPUT

    def __formatter(self, country_name: str, converted_price: str) -> tuple[str, float]:
        return (str(country_name), float(converted_price.replace("$", "")))

class dollar_price_scraper:
    def __init__(self) -> None:
        self.URL: str = "https://www.tgju.org/"
        self.RESPONSE: requests.Response = requests.get(self.URL)
        self.RESPONSE_CONTENT: bytes = self.RESPONSE.content

        self.SOUP: BeautifulSoup = BeautifulSoup(self.RESPONSE_CONTENT, "html.parser")

    def get_info(self) -> int:
        dom = etree.HTML(str(self.SOUP))
        self.DOLLAR_PRICE: int = int(str(dom.xpath('//*[@id="main"]/div[4]/div[8]/div[2]/div/div[1]/div[2]/div/div[1]/table/tbody/tr[1]/td[1]')[0].text).replace("\n", "").replace(",", ""))
        
        return self.DOLLAR_PRICE
