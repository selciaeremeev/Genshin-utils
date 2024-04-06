# coding: utf-8
import os
import sys
from loguru import logger
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from objects import markers

URL = "https://www.hoyolab.com"
USER_DATA_DIR = os.environ["GENSHIN_UTILS_USER_DATA_DIR"]  # e.g. `C:\Users\{USERNAME}\AppData\Local\Google\Chrome\User Data` (Access `chrome://version/` and check)
PROFILE_DIRECTORY = os.environ["GENSHIN_UTILS_PROFILE_DIRECTORY"]  # e.g. `Default` (Access `chrome://version/` and check)


def find_element(remote: Remote, xpath: str, timeout: int = 10) -> WebElement:
    try:
        return WebDriverWait(remote, timeout).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    except TimeoutException:
        raise TimeoutException(f"Failed to locate element within {timeout} seconds using XPath: `{xpath}`.")


def obtain_login_bonus(headless: bool = False):
    options = Options()
    if headless:
        options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=WebRtcHideLocalIpsWithMdns")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(f"--user-data-dir={USER_DATA_DIR}")
    options.add_argument(f"--profile_directory={PROFILE_DIRECTORY}")

    driver = webdriver.Chrome(options=options)

    driver.get(URL)

    if driver.execute_script("return navigator.webdriver"):
        logger.error("If it is recognized as a webdriver, further operations will be canceled.")
        driver.quit()

    find_element(driver, markers["login_bonus"]).click()

    # Switch to latest opened window (login bonus window)
    driver.switch_to.window(driver.window_handles[-1])

    try:
        find_element(driver, markers["guide_close"]).click()
    except TimeoutException:
        pass

    find_element(driver, markers["active_item"]).click()

    try:
        find_element(driver, markers["reward_tips"])
    except TimeoutException:
        raise AssertionError("Failed to obtain login bonus.")


if __name__ == "__main__":
    obtain_login_bonus("--headless" in sys.argv)
