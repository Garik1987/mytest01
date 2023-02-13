from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
import time
import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.youtube.com/")

        def test_akt01(self):
            searchFildElement = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "search_query")))
            searchFildElement.clear()
            searchFildElement.send_keys("hayat project")
            searchFildElement.send_keys(Keys.ENTER)
            time.sleep(1)
            imageButton = self.driver.find_element(By.XPATH, "(//img[@class='yt-core-image--fill-parent-height yt-core-image--fill-parent-width yt-core-image yt-core-image--content-mode-scale-aspect-fill yt-core-image--loaded'])[9]")
            imageButton.click()
            time.sleep(10)
