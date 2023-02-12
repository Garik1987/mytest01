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
        self.driver.get("https://www.google.com/webhp?hl=en")


    def test_act(self):
        searchFildElement = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "q")))
        searchFildElement.clear()
        searchFildElement.send_keys("Gyumri")
        searchFildElement.send_keys(Keys.ENTER)
        time.sleep(1)
        imageButton = self.driver.find_element(By.LINK_TEXT, "Images")
        imageButton.click()
        time.sleep(1)
        firstImage = self.driver.find_element(By.XPATH, "//img[@width='286']")
        firstImage.click()
        time.sleep(3)


        try:
            self.driver.find_element(By.XPATH, "(//img[@data-noaft='1'])[2]")

        except:
            print("Eror 5: Image not opened")
            exit(5)



    def test_act2(self):
        searchFildElement = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "q")))
        searchFildElement.clear()
        searchFildElement.send_keys("Gyumri")
        searchFildElement.send_keys(Keys.ENTER)
        time.sleep(1)
        imageButton = self.driver.find_element(By.LINK_TEXT, "Images")
        imageButton.click()
        time.sleep(1)
        firstImage = self.driver.find_element(By.XPATH, "//img[@alt='Private tour to Gyumri old town and Marmashen monastery 2023 - Yerevan']")
        firstImage.click()
        time.sleep(3)


        try:
            self.driver.find_element(By.XPATH, "(//img[@jsaction='load:XAeZkd;'])[2]")

        except:
            print("Eror 5: Image not opened")
            exit(5)


    def tearDown(self):
        self.driver.close()