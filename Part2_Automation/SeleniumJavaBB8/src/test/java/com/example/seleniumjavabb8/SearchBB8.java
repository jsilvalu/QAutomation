package com.example.seleniumjavabb8;

import org.junit.jupiter.api.Assertions;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class SearchBB8 {

    /**
     * BB8Flow
     * Performs calls to functions that automate the e2e functional flow to search for and buy product
     * @param driver
     * @throws InterruptedException
     */
    public void BB8Flow(WebDriver driver) throws InterruptedException {
        searcBB8(driver);
        buyBB8(driver);
    }

    /**
     * searcBB8
     * Search for the product and check with assertions to continue shopping in the cart.
     * @param driver
     * @throws InterruptedException
     */
    public void searcBB8(WebDriver driver) throws InterruptedException {
        WebDriverWait wait = new WebDriverWait(driver, 10000);

        // Click 'Continuar'
        driver.findElement(By.xpath("//button[. = 'Continuar']")).click();

        // Click 'Aceptar todas las Cookies'
        driver.findElement(By.xpath("//button[. = 'Aceptar todo']")).click();
        driver.findElement(By.xpath("//header/div[2]/div[2]/div[1]/div[5]/div[1]/button[1]")).click();

        // Click 'search'
        driver.findElement(By.cssSelector("#desktop-search-search-input")).click();

        // Type 'BB-8' in 'search'
        driver.findElement(By.cssSelector("#desktop-search-search-input")).sendKeys("BB-8");

        // Does 'Llavero de BB-8™ LEGO® <i>Star Wars</...' contain 'Llavero de BB-8™ LEGO® <i>Star Wars</i>™'?
        wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//p[. = 'Llavero de BB-8™ LEGO® <i>Star Wars</i>™']")));
        String suggestion = driver.findElement(By.xpath("//p[. = 'Llavero de BB-8™ LEGO® <i>Star Wars</i>™']")).getText();
        Assertions.assertTrue(suggestion.contains("Llavero de BB-8™ LEGO® <i>Star Wars</i>™"));

        // Get text from 'Llavero de BB-8™ LEGO® <i>Star Wars</...'
        driver.findElement(By.xpath("//p[. = 'Llavero de BB-8™ LEGO® <i>Star Wars</i>™']")).getAttribute("value");

        // Click 'Llavero de BB-8™ LEGO® <i>Star Wars</...'
        driver.findElement(By.xpath("//p[. = 'Llavero de BB-8™ LEGO® <i>Star Wars</i>™']")).click();

        // Get text from 'Price4,99 €'
        String price = driver.findElement(By.xpath("//div[3]//span[. = 'Price4,99 €']")).getText();
        Assertions.assertTrue(price.contains("4,99 €"));

        // Click 'Añadir a la Bolsa'
        //driver.findElement(By.xpath("//div[5]/div[1]/div/div/div/button[. = 'Añadir a la Bolsa']")).click();
        WebElement ele = driver.findElement(By.xpath("//div[5]/div[1]/div/div/div/button[. = 'Añadir a la Bolsa']"));
        JavascriptExecutor jse = (JavascriptExecutor)driver;
        jse.executeScript("arguments[0].click()", ele);

        // Click 'Ver mi bolsa'
        driver.findElement(By.xpath("//a[. = 'Ver mi bolsa']")).click();

        // Click 'Tramitar pedido de forma segura'
        driver.findElement(By.xpath("//a[. = 'Tramitar pedido de forma segura']")).click();

        // Click 'Continuar como invitado'
        driver.findElement(By.xpath("//button[. = 'Continuar como invitado']")).click();

    }

    /**
     * buyBB8
     * Complete the user's information inputs to buy the product
     * @param driver
     * @throws InterruptedException
     */
    public void buyBB8(WebDriver driver) throws InterruptedException {
        // Type 'Juan Antonio' in 'firstName'
        driver.findElement(By.cssSelector("[name='firstName']")).sendKeys("Juan Antonio");

        // Type 'Silva Luján' in 'lastName'
        driver.findElement(By.cssSelector("[name='lastName']")).sendKeys("Silva Luján");

        // Click 'INPUT' for type a address
        driver.findElement(By.xpath("//div/div/div/div/label/input")).click();

        // Type 'Avenida de Elvas' in 'INPUT'
        driver.findElement(By.xpath("//div/div/div/div/label/input")).sendKeys("Avenida de Elvas");

        // Click 'Avenida de Elvas, 06006 Badajoz'
        driver.findElement(By.cssSelector("#suggestion-0")).click();

        // Click 'Dirección de envío'
        driver.findElement(By.xpath("//button[. = 'Dirección de envío']")).click();

        // Click 'Continuar' to email
        driver.findElement(By.xpath("//button[. = 'Continuar']")).click();

        // Type 'jsilvalu93@gmail.com' in 'email'
        driver.findElement(By.cssSelector("[name='email']")).sendKeys("jsilvalu93@gmail.com");

        // Type '622294965' in 'phone'
        driver.findElement(By.cssSelector("[name='phone']")).sendKeys("622294965");

        // Click 'Continuar a Pago'
        driver.findElement(By.xpath("//button[. = 'Continuar a Pago']")).click();

    }
}
