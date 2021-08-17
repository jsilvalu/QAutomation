package com.example.seleniumjavabb8;

import com.example.seleniumjavabb8.configDriver.ConfigDriver;
import org.junit.jupiter.api.*;
import org.openqa.selenium.*;
import java.io.IOException;
import java.util.concurrent.TimeUnit;

public class MainPageTest {
    private WebDriver driver;

    @BeforeEach
    public void setUp() throws InterruptedException {
        //WebDriverManager.chromedriver().setup();
        //driver = new ChromeDriver();

        ConfigDriver config = new ConfigDriver();
        driver = config.getWebDriverReady(driver);
        driver.manage().window().maximize();
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
        driver.get("https://www.lego.com/es-es");

    }

    @AfterEach
    public void tearDown() {
        driver.quit();
    }

    @Test
    public void searchBB8() throws InterruptedException, IOException {
        SearchBB8 s = new SearchBB8();
        s.BB8Flow(driver);
    }

}
