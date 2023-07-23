import re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import requests as r
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)


def is_instagram_reels_url(url) -> bool:
    """
    Check the url is instagram reels url?
    :param url: instagram reels url
    :return: bool
    """
    pattern = r"https?://(?:www\.)?instagram\.com/reel/.*"

    match = re.match(pattern, url)
    if match:
        return True
    return False


def download_reels(url) -> bytes:
    """
    Download reels video and massage

    :param url: instagram reels url
    :return: bytes
    """
    driver.get(url)

    wait = WebDriverWait(driver, 10)

    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'video')))

    reel_source = element.get_attribute('src')

    return r.get(reel_source).content
