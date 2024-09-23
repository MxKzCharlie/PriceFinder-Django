"""Hola"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from django.test import LiveServerTestCase

class MySeleniumTest(LiveServerTestCase):

    def setUp(self):
        self.opts = Options()
        self.opts.add_argument(
            "user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36"
        )
        self.opts.add_argument("--disable-search-engine-choice-screen")
        self.opts.add_argument("--headless")
        self.opts.add_argument("--disable-gpu")
        self.opts.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.opts)

    def tearDown(self):
        self.driver.quit()

    def test_mercado_libre_scraping(self):
        self.driver.get('https://www.mercadolibre.com.mx/')
        sleep(4)

        # Manejar el disclaimer
        try:
            disclaimer = self.driver.find_element(By.XPATH, '//button[@id="download-app-bottom-banner-close"]')
            disclaimer.click()
        except Exception as e:
            print(e)

        sleep(3)

        value = 'audifonos bluetooth'
        search = self.driver.find_element(By.XPATH, '//input[@id="cb1-edit"]')
        search.send_keys(value)
        sleep(1)

        option = self.driver.find_element(By.XPATH, '//li[@id="cb1-opt1-1"]')
        option.click()
        sleep(4)

        links_products = self.driver.find_elements(By.XPATH, '//div[@class="ui-row-item-info"]/a')

        links_per_product = [tag_a.get_attribute("href") for tag_a in links_products]

        data = []

        quantity = min(len(links_per_product), 7)
        for i in range(0, quantity):
            try:
                self.driver.get(links_per_product[i])
                titulo = self.driver.find_element(By.XPATH, '//h1[@class="ui-pdp-title"]')
                precio = self.driver.find_element(By.XPATH, '//*[@id="root-app"]/div[2]/div[3]/div[3]/div[13]/div/div/div[1]/div[1]/span[1]/span/span[2]')
                img = self.driver.find_element(By.XPATH, '//img[contains(@class, "ui-pdp-image ui-pdp-gallery")]')
                url_img = img.get_attribute('src')
                data.append({
                    "title": titulo.text, 
                    "price": precio.text, 
                    "url_img": url_img})
                self.driver.back()
            except Exception as e:
                print(e)
                self.driver.back()    
        