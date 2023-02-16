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
            videoButton = self.driver.find_element(By.XPATH, "(//*[@class='style-scope ytd-video-renderer'])[1]")
            videoButton.click()
            time.sleep(15)
            videoButton1 = self.driver.find_element(By.XPATH,"(//video[@class='video-stream html5-main-video'])")
            videoButton1.click()
            time.sleep(3)

    def tearDown(self):
        self.driver.close()