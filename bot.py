from dbOperation import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from config import telegram_bot_api
import os

dyno_usage_reset()
while True:
    init_time = time.time()
    ### for heroku ###

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(
        executable_path=os.environ.get("CHROMEDRIVER_PATH"),
        chrome_options=chrome_options,
    )
    #### for heroku ###

    driver = webdriver.Chrome("./chromedriver")

    driver.implicitly_wait(5)
    driver.set_page_load_timeout(20)

    driver.get("http://coochbeharcollege.org.in/notice.aspx")
    x = driver.page_source  # page source code to process.

    dbData = getter()  # get data from database

    x = x[x.find("<table>") : x.find("</table>")]  # get full table
    temp = ""
    k = 1
    for i in range(len(x)):
        if x.startswith("popuplink", i):
            # print(x[i : i + 13])
            j = i
            temp = x[j : j + 13]

            if dbData.count(temp) == 0:
                # print("do operation")
                # for caption
                capt = driver.find_element(By.ID, temp).text
                # document.getElementById("popuplink4116").text
                # print(capt)

                driver.find_element(By.ID, temp).click()
                # time.sleep(2)
                ele = driver.find_element_by_class_name("bd").get_attribute("outerHTML")
                url_base_index = ele.index(
                    'onclick="JavaScript:view(this.title)" title="'
                )
                url_end_index = ele.index(">View</a>")

                title = ele[url_base_index + 45 : url_end_index - 1]
                # print(title)
                title = title.replace(" ", "%20")
                # print(title)
                title = "http://coochbeharcollege.org.in/UploadedFiles/" + title
                # if title.count("amp;") > 0:
                #     title = title.replace("amp;", "")

                ##### bug exists

                # print(title)
                # time.sleep(1)

                chat_id = -1001381972668

                driver.refresh()
                print(k, ": ", title)
                k += 1
                url = f"https://api.telegram.org/bot{telegram_bot_api}/sendDocument?chat_id={chat_id}&caption={capt}&document={title}"
                print(url)
                time.sleep(1)
                response = requests.get(url)
                if response.status_code == 400:
                    txt = f"New Notice available. Bot unable to download it. \n\nkindly visit: https://coochbeharcollege.org.in/notice.aspx  \n\nNotice title: {capt}"
                    requests.get(
                        f"https://api.telegram.org/bot{telegram_bot_api}/sendMessage?chat_id={chat_id}&text={txt}"
                    )

                # insert into database
                setter(temp)
            else:
                continue

    print("I'm alive! will update you in next 5 seconds.")
    x = ""
    driver.quit()
    time.sleep(5)
    final_time = time.time()
    time_taken = final_time - init_time
    dyno_usage_response = dyno_usage_setter(time_taken)
    
    if dyno_usage_response == -1:
        # dyno 440 hours used kindly chnage it.
        txt = f"@anantapodder I'll die if you don't change dyno within next 9 hours."
        requests.get(
            f"https://api.telegram.org/bot{telegram_bot_api}/sendMessage?chat_id={chat_id}&text={txt}"
        )
    elif dyno_usage_response == -2:
        # dyno 449 hours used kindly chnage it.
        txt = f"@anantapodder I'll die if you don't change dyno within next 59 minutes."
        requests.get(
            f"https://api.telegram.org/bot{telegram_bot_api}/sendMessage?chat_id={chat_id}&text={txt}"
        )

print("Exiting")