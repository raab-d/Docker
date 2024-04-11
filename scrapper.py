import time
import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

url = "https://www.pokecardex.com/series"


def setup_driver():
#/config
    useragent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 "
                 "Safari/537.36")

    options = ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    prefs = {"credentials_enable_service": False,
             "profile.password_manager_enabled": False}

    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": useragent})

    return driver


def get_cards(serie, driver):
    print(serie.text)

    if not os.path.exists(f'data/raw_HD/{serie.text}'):
        os.makedirs(f"data/raw_HD/{serie.text}")

    xpath = f'//*[@id="{serie.text}"]/div/div/div'
    container = driver.find_element(By.XPATH, xpath)

    cards = container.find_elements(By.CLASS_NAME, "col-lg-3")

    driver2 = setup_driver()

    for card in cards:
        a_tag = card.find_element(By.CLASS_NAME, "d-block")
        # get href value of a tag
        link = a_tag.get_attribute("href")

        driver2.get(link)

        time.sleep(2)

        try:
            cookies_btn = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]/p")

            cookies_btn.click()
        except:
            print("No cookies button found")

        cards_image = driver2.find_elements(By.CLASS_NAME, "br-10")
        print(len(cards_image))
        for card_image in cards_image:
            try:
                src = card_image.get_attribute("src")
                print(src)

                set_name = src.split("/")[-2]

                filename = src.split("/")[-1]

                if not os.path.exists(f'data/raw_HD/{serie.text}/{set_name}'):
                    os.makedirs(f'data/raw_HD/{serie.text}/{set_name}')

                    # Save image in directory

                hd_src = '/'.join(src.split("/")[0:-1]) + "/HD/" + src.split("/")[-1]

                r = requests.get(hd_src, allow_redirects=True)

                open(f'/usr/src/scrapper/data/raw_HD/{serie.text}/{set_name}/{filename}', "wb").write(r.content)

            except:
                print("No src attribute found")


def get_series():
    driver = setup_driver()

    driver.get(url)

    time.sleep(2)

    try:
        cookies_btn = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]/p")

        cookies_btn.click()
    except:
        print("No cookies button found")

    series = driver.find_elements(By.CLASS_NAME, "p-0")

    for serie in series:
        if serie.text != "":
            get_cards(serie, driver)

    time.sleep(5)

    driver.quit()


get_series()
