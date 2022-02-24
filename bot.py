from dis import findlabels
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from sqlalchemy import true

driver = webdriver.Chrome("./chromedriver")
# # driver = webdriver.Edge("./msedgedriver")

driver.implicitly_wait(5)
driver.set_page_load_timeout(20)

driver.get("http://coochbeharcollege.org.in/notice.aspx")
# driver.get_screenshot_as_file("xyz.png")
pageSource = driver.page_source
fileToWrite = open("page_source.html", "w")
fileToWrite.write(pageSource)
fileToWrite.close()
fileToRead = open("page_source.html", "r")
x = fileToRead.read()
fileToRead.close()


x = x[x.find("<table>") : x.find("</table>")]  # get full table
temp = ""
for i in range(len(x)):
    if x.startswith("popuplink", i):
        # print(x[i : i + 13])
        temp = x[i : i + 13]

print(temp)

driver.find_element(By.ID, temp).click()
time.sleep(5)
# xyz = driver.find_element(
#     By.XPATH,
#     "/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/div/div/div[1]/div[2]/div/table/tbody/tr[4]/td/table/tbody/tr/td[3]/a",
# )
# print(xyz)
ele = driver.find_element_by_class_name("bd").get_attribute("outerHTML")
# print(ele)

url_base_index = ele.index('onclick="JavaScript:view(this.title)" title="')
url_end_index = ele.index(">View</a>")

title = ele[url_base_index + 45 : url_end_index - 1]
# print(title)
title = title.replace(" ", "%20")
# print(title)
title = "http://coochbeharcollege.org.in/UploadedFiles/" + title
print(title)


time.sleep(10)

# from urllib import response
# import requests

# requests.get(
#     "http://coochbeharcollege.org.in/Download.aspx?file=UploadedFiles/522301AREVISED%20NOTICE%20FOR%201ST%20SEMESTER%20M%20A%20%20M%20SC%20ONLINE%20EXAM%20FORM%20FILLUP%202022.pdf"
# )

import requests

# url = "http://coochbeharcollege.org.in/Download.aspx?file=UploadedFiles/522301AREVISED%20NOTICE%20FOR%201ST%20SEMESTER%20M%20A%20%20M%20SC%20ONLINE%20EXAM%20FORM%20FILLUP%202022.pdf"
# response = requests.get(url, stream=True)

# with open("./metadata.pdf", "wb") as f:
#     f.write(response.content)

# url = "https://api.telegram.org/bot5230528864:AAE0oT9CEjczbzSj4MGugvmmZzKEl5mXXGQ/sendDocument?chat_id=@testananta&document='http://coochbeharcollege.org.in/Download.aspx?file=UploadedFiles/522301AREVISED%20NOTICE%20FOR%201ST%20SEMESTER%20M%20A%20%20M%20SC%20ONLINE%20EXAM%20FORM%20FILLUP%202022.pdf'"
# response = requests.get(url)
# print(response)
driver.quit()