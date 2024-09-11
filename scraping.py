from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
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

        self.USA: WebElement = self.TABLE.find_element(By.XPATH, '//*[@id="prices"]/div[4]/div[1]/table/tbody/tr[1]')
        self.BRAZIL: WebElement = self.TABLE.find_element(By.XPATH, '//*[@id="prices"]/div[4]/div[1]/table/tbody/tr[2]')
        self.UKRAINE: WebElement = self.TABLE.find_element(By.XPATH, '//*[@id="prices"]/div[4]/div[1]/table/tbody/tr[3]')
        self.CHINA: WebElement = self.TABLE.find_element(By.XPATH, '//*[@id="prices"]/div[4]/div[1]/table/tbody/tr[6]')
        self.TAIWAN: WebElement = self.TABLE.find_element(By.XPATH, '//*[@id="prices"]/div[4]/div[1]/table/tbody/tr[13]')
        self.PHILLIPINES: WebElement = self.TABLE.find_element(By.XPATH, '//*[@id="prices"]/div[4]/div[1]/table/tbody/tr[25]')
        self.RUSSIA: WebElement = self.TABLE.find_element(By.XPATH, '//*[@id="prices"]/div[4]/div[1]/table/tbody/tr[41]')
        
        self.COUNTRIES: list[WebElement] = [self.USA, self.BRAZIL, self.UKRAINE, self.CHINA, self.TAIWAN, self.PHILLIPINES, self.RUSSIA]
        
        for _, country in enumerate(self.COUNTRIES):
            print(country.text)
       

if __name__ == "__main__":
    SCRAPER: scraper = scraper()

