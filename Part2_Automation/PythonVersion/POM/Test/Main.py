import argparse
import json
import os
import sys
import unittest
import pytest

from pyunitreport import HTMLTestRunner
from Drivers.configDriver import configDriver
from POM.Products.BB8 import BB8

sys.path.append(os.path.join(os.path.dirname(__file__), "../../..", ".."))

# Pytests variables
browser = "chrome"
headless_browser = "default"
page_load_strategy = "default"
resolucion = "default"
output = "default"


class Main(unittest.TestCase):

    @classmethod
    def setUp(cls):

        config = cls.get_json_data()  # Reading the json configuration file

        # Webdriver configuration
        cls.driver = configDriver.get_webdriver(browser, config, headless_browser, page_load_strategy)
        driver = cls.driver

        if headless_browser == "default":  # Webdriver resolution settings
            configDriver.config_resolution(driver, resolucion)

        driver.implicitly_wait(20)  # Implicit 30-second wait assignment

        driver.get(config['BROWSER']['URL'])

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    @pytest.mark.skipif(False, reason="Skip Test --- ")
    def test_case_search_buy_BB8(self):
        """
        test_bB8
        :Perform the e2e flow of search and purchase of a BB8 keychain
        """
        BB8(self.driver, data_json=self.get_json_data())

    @staticmethod
    def get_json_data():
        """
        Access the JSON data.json in ../../Data to get an instance of the contents of the configuration files.
        """
        # Lectura del fichero de configuracion json
        with open('../../Data/data.json', 'r', encoding="utf-8") as file:
            config = json.load(file)
        return config


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--browser", default="chrome",
                        help="Browser in which to run the tests - {chrome, firefox, edge, opera}")
    parser.add_argument("-r", "--resolution", default="default",
                        help="Browser resolution at which to run the tests -  {ancho x alto}")
    parser.add_argument("-s", "--page_load_strategy", default="normal",
                        help="Page loading strategy, ONLY compatible with chrome (default) and firefox -  {"
                             "normal, eager, none}")
    parser.add_argument("-l", "--headless_browser", default="default",
                        help="Headless browser mode, ONLY compatible with chrome (default) and firefox - {headless}")
    parser.add_argument("-path", "--output_path_evidences", default="default",
                        help="Path where to save the evidences (captures and report) {path}")
    args = parser.parse_args()

    # Aquí procesamos lo que se tiene que hacer con cada argumento
    if args.browser:
        browser = args.browser
        print("[info] WebDriver: " + browser)
    if args.resolution:
        resolucion = args.resolution
        print("[info] Resolution : " + resolucion)
    if args.page_load_strategy:
        page_load_strategy = args.page_load_strategy
        print("[info] Page loading strategy: " + page_load_strategy)
    if args.headless_browser:
        headless_browser = args.headless_browser
        print("[info] Headless browser : " + headless_browser)
    if args.output_path_evidences:
        output = args.output_path_evidences
        print("[info] Output : " + output)
    if output == "default":
        output_path_report = '../../Evidences/reportHTML'
    else:
        try:
            os.stat(output + '/reportHTML')
        except:
            os.makedirs(output + '/reportHTML', exist_ok=True)
        output_path_report = output + '/reportHTML'

    # Launch of test suites with evidence collection
    unittest.main(verbosity=3, argv=['first-arg-is-ignored'],
                  testRunner=HTMLTestRunner(output=os.getcwd() + "\Evidences\ReportHTML",
                                            report_title="Selenium Test in LEGO.com - "
                                                         "   Browser: " + browser +
                                                         ",  Resolution: " + resolucion +
                                                         ",  Mode: " + headless_browser +
                                                         ",  Strategy: " + page_load_strategy +
                                                         ",  Output: " + output))
