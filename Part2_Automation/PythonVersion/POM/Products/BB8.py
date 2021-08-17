import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BB8:

    def __init__(self, driver, data_json):

        driver.get_screenshot_as_file('Evidences/ScreenShots/home.png')
        driver.find_element(By.XPATH, "//button[. = 'Continuar']").click()  # Click on 'Continuar'
        driver.find_element(By.XPATH, "//button[. = 'Aceptar todo']").click()  # Click on 'Aceptar coockies'

        self.search_product(driver, data_json)
        self.product_details(driver, data_json)
        self.cart(driver, data_json)

    def search_product(self, driver, data_json):
        """
        search_product
        :param driver:
        :return: None
        """
        driver.find_element(By.XPATH, "//div[5]/div/button/*[name()='svg']").click()

        # Type 'BB-8' in 'search'
        driver.find_element(By.CSS_SELECTOR, "#desktop-search-search-input").send_keys("BB-8")

        # Does 'Llavero de BB-8™ LEGO® <i>Star Wars</...' contain 'Llavero de BB-8™ LEGO® <i>Star Wars</i>™'?
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//p[. = 'Llavero de BB-8™ LEGO® <i>Star Wars</i>™']")))
        suggestion = driver.find_element(By.XPATH, "//p[. = 'Llavero de BB-8™ LEGO® <i>Star Wars</i>™']").text
        driver.get_screenshot_as_file('Evidences/ScreenShots/searchingBB8.png')

        # Get text from 'Llavero de BB-8™ LEGO® <i>Star Wars</...'
        value = driver.find_element(By.XPATH, "//p[. = 'Llavero de BB-8™ LEGO® <i>Star Wars</i>™']").get_attribute("value")

        # Click 'Llavero de BB-8™ LEGO® <i>Star Wars</...'
        driver.find_element(By.XPATH, "//p[. = 'Llavero de BB-8™ LEGO® <i>Star Wars</i>™']").click()

        # Get text from 'Price4,99€'
        price = driver.find_element(By.XPATH, "//div[3]//span[. = 'Price4,99 €']").get_attribute("value")

    def product_details(self, driver, data_json):
        """
        product_details
        :param driver:
        :return: None
        """
        # Click on 'Añadir a la Bolsa'
        driver.find_element(By.XPATH, "//div[5]/div[1]/div/div/div/button/div[. = 'Añadir a la Bolsa']").click()

        # Click on 'Ver mi bolsa'
        driver.find_element(By.XPATH, "//a[. = 'Ver mi bolsa']").click()

        # Click on 'Tramitar pedido de forma segura'
        driver.find_element(By.XPATH, "//a[. = 'Tramitar pedido de forma segura']").click()
        driver.get_screenshot_as_file('Evidences/ScreenShots/goPayment.png')

    def cart(self, driver, data_json):
        """
        cart
        :param driver:
        :return: None
        """
        driver.find_element(By.XPATH, "//button[. = 'Continuar como invitado']").click()

        # Type 'Juan Antonio' in 'firstName'
        driver.find_element(By.CSS_SELECTOR, "[name='firstName']").send_keys(data_json["CREDENTIALS"]["first_name"])

        # Type 'Silva Luján' in 'lastName'
        driver.find_element(By.CSS_SELECTOR, "[name='lastName']").send_keys(data_json["CREDENTIALS"]["last_name"])

        # Type 'Avenida de Elvas' in 'INPUT'
        driver.find_element(By.XPATH, "//div/div/div/div/label/input").send_keys(data_json["CREDENTIALS"]["address"])

        driver.get_screenshot_as_file('Evidences/ScreenShots/personalData.png')

        # Click 'Avenida de Elvas, 06006 Badajoz'
        driver.find_element(By.CSS_SELECTOR, "#suggestion-0").click()

        # Click 'Dirección de envío'
        driver.find_element(By.XPATH, "//button[. = 'Dirección de envío']").click()

        # Click 'Continuar1'
        driver.find_element(By.XPATH, "//button[. = 'Continuar']").click()

        # Type 'jsilvalu93@gmail.com' in 'email'
        driver.find_element(By.CSS_SELECTOR, "[name='email']").send_keys(data_json["CREDENTIALS"]["email"])

        # Type '622294965' in 'phone'
        driver.find_element(By.CSS_SELECTOR, "[name='phone']").send_keys(data_json["CREDENTIALS"]["user_phone"])

        driver.get_screenshot_as_file('Evidences/ScreenShots/goPayment.png')

        # Click 'Continuar a Pago'
        driver.find_element(By.XPATH, "//button[. = 'Continuar a Pago']").click()

