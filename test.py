import requests
from bs4 import BeautifulSoup



result = requests.get('https://kr.indeed.com/jobs?q=python&start=0')
soup = BeautifulSoup(result.text, "html.parser")
# results = soup.find_all("h2", {"class": "jobTitle"})
results = soup.find_all("div", {"id": "mosaic-provider-jobcards"})
#print(results)
#print(results.find_all("span").get("title"))
print(results.find_all("span"))