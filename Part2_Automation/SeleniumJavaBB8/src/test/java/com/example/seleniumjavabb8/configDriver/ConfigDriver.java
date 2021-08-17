package com.example.seleniumjavabb8.configDriver;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.edge.EdgeOptions;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.firefox.FirefoxOptions;
import org.openqa.selenium.opera.OperaDriver;
import org.openqa.selenium.opera.OperaOptions;
import org.openqa.selenium.remote.DesiredCapabilities;

public class ConfigDriver {

    /**/
    Browsers b;
    int widthResolution;
    int higResolution;
    boolean maxWindows;
    boolean headlessMode;


    public ConfigDriver(){
        this.b = Browsers.CHROME;
        this.widthResolution = 0;
        this.higResolution = 0;
        this.maxWindows = true;
        this.headlessMode = false;
    }

    public ConfigDriver(Browsers b, int widthResolution, int higResolution, boolean maxWindows, boolean headlessMode) {
        this.b = b;
        this.widthResolution = widthResolution;
        this.higResolution = higResolution;
        this.maxWindows = maxWindows;
        this.headlessMode = headlessMode;
    }

    /**
     * setCustomResolution
     * Assigns the capability to set the browser's screen resolution
     * @param driver
     */
    public void setCustomResolution(WebDriver driver){

        DesiredCapabilities caps = new DesiredCapabilities();

        if(this.maxWindows){
            driver.manage().window().maximize();
        }else{
            caps.setCapability("resolution", this.widthResolution+"x"+this.higResolution);
        }
    }

    /**
     * getWebDriverReady
     * Configure and return a webdriver depending on the object (Chrome, Firefox, Edge, Opera) via WebDriver Manager,
     * also set options and headless mode if desired.
     * @param driver
     * @return driver
     */
    public WebDriver getWebDriverReady(WebDriver driver){

        if(this.b == Browsers.CHROME)   {
            WebDriverManager.chromedriver().setup();
            driver = new ChromeDriver();
            if(this.headlessMode)  {
                ChromeOptions options = new ChromeOptions();
                options.addArguments("--headless");
                options.addArguments("--window-size=1920,1080");
                options.addArguments("--ignore-certificate-errors");
                options.addArguments("--disable-extensions");
                options.addArguments("--proxy-server='direct://'");
                options.addArguments("--proxy-bypass-list=*");
                options.addArguments("--start-maximized");
                options.addArguments("--disable-gpu");
                options.addArguments("--disable-dev-shm-usage");
                options.addArguments("--no-sandbox");

                driver = new ChromeDriver(options);
            }
            return driver;

        } else if (this.b == Browsers.FIREFOX) {
            WebDriverManager.firefoxdriver().setup();
            driver = new FirefoxDriver();
            if(this.headlessMode)  {
                FirefoxOptions options = new FirefoxOptions();
                options.addArguments("--headless");
                options.addArguments("--window-size=1920,1080");
                options.addArguments("--ignore-certificate-errors");
                options.addArguments("--disable-extensions");
                options.addArguments("--proxy-server='direct://'");
                options.addArguments("--proxy-bypass-list=*");
                options.addArguments("--start-maximized");
                options.addArguments("--disable-gpu");
                options.addArguments("--disable-dev-shm-usage");
                options.addArguments("--no-sandbox");
                driver = new FirefoxDriver(options);
            }
            return driver;

        } else if (this.b == Browsers.EDGE) {
            WebDriverManager.edgedriver().setup();
            driver = new EdgeDriver();
            return driver;

        } else if (this.b == Browsers.OPERA){
            WebDriverManager.operadriver().setup();
            driver = new OperaDriver();
            if(this.headlessMode)  {
                OperaOptions options = new OperaOptions();
                options.addArguments("--headless");
                options.addArguments("--window-size=1920,1080");
                options.addArguments("--ignore-certificate-errors");
                options.addArguments("--disable-extensions");
                options.addArguments("--proxy-server='direct://'");
                options.addArguments("--proxy-bypass-list=*");
                options.addArguments("--start-maximized");
                options.addArguments("--disable-gpu");
                options.addArguments("--disable-dev-shm-usage");
                options.addArguments("--no-sandbox");
                driver = new OperaDriver(options);
            }
            return driver;
        }
        return driver;
    }

    public Browsers getB() {
        return b;
    }

    public int getWidthResolution() {
        return widthResolution;
    }

    public int getHigResolution() {
        return higResolution;
    }

    public boolean isMaxWindows() {
        return maxWindows;
    }

    public boolean isHeadlessMode() {
        return headlessMode;
    }

    public void setB(Browsers b) {
        this.b = b;
    }

    public void setWidthResolution(int widthResolution) {
        this.widthResolution = widthResolution;
    }

    public void setHigResolution(int higResolution) {
        this.higResolution = higResolution;
    }

    public void setMaxWindows(boolean maxWindows) {
        this.maxWindows = maxWindows;
    }

    public void setHeadlessMode(boolean headlessMode) {
        this.headlessMode = headlessMode;
    }
}
