import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
url = 'https://www.naukri.com/financial-analyst-jobs-in-mumbai?k=financial%20analyst&l=mumbai'

page = requests.get(url).text

driver = webdriver.Chrome(c)
driver.get(url)
time.sleep(3)
soup = BeautifulSoup(driver.page_source,'html5lib')
print(soup.prettify())
driver.close()

df = pd.DataFrame(columns=['Title','Company','Ratings','Reviews','URL'])
results = soup.find(class_='list')

job_elems = results.find_all('article',class_='jobTuple bgWhite br4 mb-8')

for job_elem in job_elems:
    URL=job_elem.find('a',class_='title fw500 ellipsis').get('href')
    print(URL)
    Title=job_elem.find('a',class_='title fw500 ellipsis')
    print(Title)

    rating_span=job_elem.find('span',class_='starRating fleft dot')
    if rating_span is None:
        continue
    else:
        Rattings=rating_span.text
    print(Rattings)

    Review_span=job_elem.find('a',class_='reviewsCount ml-5 fleft blue-text')
    if Review_span is None:
        continue
    else:
        Reviews=Review_span.text
    print(Reviews)

