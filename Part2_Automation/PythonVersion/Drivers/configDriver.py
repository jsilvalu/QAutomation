import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.opera.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager


class configDriver:

    @staticmethod
    def get_webdriver(browser, config, headless_browser, page_load_strategy):
        """
        :configDriver Returns a webdriver object of the particular browser to be executed from a STRING received as
        arguments during launch. If the headless_browser parameter has
        the value 'headless' then it sends a series of parameters from the config data to assign the
        assign the browser to headless browser mode.
        :param browser: main launch argument string, it indicates which browser to run.
        :param config: json file read buffer
        :param headless_browser: Its 'headless' value sends a series of parameters based on the data from the
        config data to assign the browser to headless browser mode.
        :param page_load_strategy:
        :returns Objeto webdriver
        """
        # Obtenemos el nombre del sistema para retornar webdrivers de windows o linux

        if browser == 'chrome' or browser == 'default':

            if headless_browser == 'headless':

                user_agent = config["HEADLESS_ARGUMENTS"]["user_agent"]
                chromeoptions = webdriver.ChromeOptions()
                chromeoptions.add_argument("--headless")
                chromeoptions.add_argument(f'user-agent={user_agent}')
                # annadimos todos los argumentos para ejecutar en modo headless browser con seguridad
                chromeoptions.add_argument(config["HEADLESS_ARGUMENTS"]["window-size"])
                chromeoptions.add_argument(config["HEADLESS_ARGUMENTS"]["ignore-errors:"])
                chromeoptions.add_argument(config["HEADLESS_ARGUMENTS"]["allow-running"])
                chromeoptions.add_argument(config["HEADLESS_ARGUMENTS"]["disable-extensions"])
                chromeoptions.add_argument(config["HEADLESS_ARGUMENTS"]["proxy-server"])
                chromeoptions.add_argument(config["HEADLESS_ARGUMENTS"]["proxy-bypass"])
                chromeoptions.add_argument(config["HEADLESS_ARGUMENTS"]["maximized"])
                chromeoptions.add_argument(config["HEADLESS_ARGUMENTS"]["disable-gpu"])
                chromeoptions.add_argument(config["HEADLESS_ARGUMENTS"]["disable-dev"])
                chromeoptions.add_argument(config["HEADLESS_ARGUMENTS"]["no-sandbox"])

                if page_load_strategy != "default":
                    chromeoptions.page_load_strategy = page_load_strategy  # Options: normal, eager, none

                return webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chromeoptions)
            else:
                return webdriver.Chrome(executable_path=ChromeDriverManager().install())

        if browser == 'firefox':

            if headless_browser == "headless":
                user_agent = config["HEADLESS_ARGUMENTS"]["user_agent"]
                firefox_options = webdriver.FirefoxOptions()
                firefox_options.headless = True
                firefox_options.add_argument(f'user-agent={user_agent}')
                firefox_options.add_argument(config["HEADLESS_ARGUMENTS"]["window-size"])
                firefox_options.add_argument(config["HEADLESS_ARGUMENTS"]["ignore-errors:"])
                firefox_options.add_argument(config["HEADLESS_ARGUMENTS"]["allow-running"])
                firefox_options.add_argument(config["HEADLESS_ARGUMENTS"]["disable-extensions"])
                firefox_options.add_argument(config["HEADLESS_ARGUMENTS"]["proxy-server"])
                firefox_options.add_argument(config["HEADLESS_ARGUMENTS"]["proxy-bypass"])
                firefox_options.add_argument(config["HEADLESS_ARGUMENTS"]["maximized"])
                firefox_options.add_argument(config["HEADLESS_ARGUMENTS"]["disable-gpu"])
                firefox_options.add_argument(config["HEADLESS_ARGUMENTS"]["disable-dev"])
                firefox_options.add_argument(config["HEADLESS_ARGUMENTS"]["no-sandbox"])

                if page_load_strategy != "default":
                    firefox_options.page_load_strategy = page_load_strategy  # Options: normal, eager, none

                return webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=firefox_options)
            else:
                return webdriver.Firefox(executable_path=GeckoDriverManager().install())

        if browser == 'opera':
            return webdriver.Opera(executable_path=OperaDriverManager().install())

        if browser == 'edge':  # TODO: check for Windows < 8.1?
            edgedriver = EdgeChromiumDriverManager()
            return webdriver.Edge(edgedriver.install())

    @staticmethod
    def config_resolution(driver, resolucion):
        """
        :config_resolution
        :param driver:
        :param resolucion:
        """
        if resolucion == 'default':
            driver.maximize_window()
        else:
            ancho_alto = resolucion.split('x')
            ancho, alto = ancho_alto[0], ancho_alto[1]
            driver.set_window_size(ancho, alto)

    @staticmethod
    def loading_strategy(browser, page_load_strategy):
        """
        :loading_strategy Defines the page loading strategy for the current session. By default, when
        Selenium WebDriver loads a page, it follows the normal page loading strategy. It is recommended to stop
        downloading of additional resources (such as images, css, js) when the page load takes a long time.
        a long time. By default, WebDriver will wait to respond to a driver.get() or driver.navigate().to() call
        until the document ready state is complete.
        :options 'normal'
        :options 'eager'
        :options 'none'
        :param page_load_strategy:
        :param browser: string de argumentos de lanzamiento principal
        :returns
        """
        options = Options()

        if browser == 'chrome' or browser == 'default':
            return webdriver.Chrome(options=options)

        if browser == 'firefox':
            return webdriver.Firefox(options=options)

        if browser == 'opera':
            return webdriver.Opera(options=options)

        if browser == 'edge':
            return webdriver.Edge(options=options)
