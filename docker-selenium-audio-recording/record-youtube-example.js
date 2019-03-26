var webdriver = require('selenium-webdriver'),
    By = webdriver.By,
    until = webdriver.until;

var driver = new webdriver.Builder()
    .forBrowser('chrome')
    .usingServer('http://localhost:4444/wd/hub')
    .build();

driver.get('https://www.youtube.com/watch?v=n8lpLgWrHGQ');
driver.sleep(1000 * 5);
driver.quit();
