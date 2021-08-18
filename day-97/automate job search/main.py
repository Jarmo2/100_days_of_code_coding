import time
from selenium import webdriver
import smtplib
import os
from email.mime.text import MIMEText
import datetime

##webscraper

#setup
chrome_driver_path = r"C:\Users\jarmo\Desktop\Data science\browserdriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
current_job_search = "Python Quereinsteiger"
website_short_cut = driver.get("https://de.indeed.com/jobs?q=Python+Quereinsteiger&fromage=7")
time.sleep(2)
cookies = driver.find_element_by_id("onetrust-accept-btn-handler")
cookies.click()
time.sleep(1)
jobs = driver.find_elements_by_css_selector("a[class^='tapItem fs-unmask result job']")
time.sleep(2)
counter = 1

#creation of html
for element in jobs:
    element.click()
    time.sleep(3)
    details = driver.find_elements_by_css_selector("div[id^='vjs-tab-job']")[0].text
    with open(f"job_summary.html", 'a', encoding="utf-8") as current_page:
        current_page.write(str(f"<h1>{counter}</h1>"))
        current_page.write(str(f"<p>{details}</p>"))
    time.sleep(2)
    counter += 1


##email tool
fromaddr = os.environ.get('gmail_user')
toaddr = "luxuspinguin@outlook.de"
date = datetime.date.today().strftime("%d/%m/%Y")

html = open("job_summary.html", encoding='utf-8')
msg = MIMEText(html.read(), 'html')
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = f"Job on Indeed as per {date}"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(os.environ.get('gmail_user'), os.environ.get('gmail_pw'))
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

html.close()

os.remove('job_summary.html')





