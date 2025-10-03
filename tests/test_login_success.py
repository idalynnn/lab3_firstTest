from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_success(driver):
    page = Path(__file__).resolve().parents[1] / "login.html"
    driver.get(page.as_uri())

    driver.find_element(By.ID, "username").send_keys("123")
    driver.find_element(By.ID, "password").send_keys("123")
    driver.find_element(By.ID, "login-btn").click()

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "logout"))
    )
