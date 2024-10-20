from selenium import webdriver
import pytest

@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_website_load(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    
    driver.get("http://127.0.0.1:8000/")
    assert "Stripe" in driver.title
    driver.quit()
