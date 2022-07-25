from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import config
import os


list_profile= []




def get_acount():
    dirs = next(os.walk(config.PROFILE_DIR), ([], [], []))[1]
    for elem in dirs:
        if "Profile " in elem:
            list_profile.append(elem)





get_acount()
for profile in list_profile:
    options = Options()
    options.add_argument("--allow-profiles-outside-user-dir")
    options.add_argument(f"--profile-directory={profile}")
    options.add_argument(f"user-data-dir={config.PROFILE_DIR}")
    driver = webdriver.Chrome(executable_path=config.CHROME_DRRIVER_PATH, options=options)
    driver.get("https://www.instagram.com")
    print(profile)