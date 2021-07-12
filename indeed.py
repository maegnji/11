import requests
from bs4 import BeautifulSoup

LIMIT = 10
URL = f'https://kr.indeed.com/jobs?q=python'


# URL_SEARCH = f'https://kr.indeed.com/jobs?q=python&start={LIMIT}'


def extract_indeed_pages():
    result = requests.get(URL)
    # print(indeed_result.status_code)
    # print(indeed_result.headers['content-type'])
    soup = BeautifulSoup(result.text, "html.parser")
    # print(indeed_soup)
    pagination = soup.find("div", {"class": 'pagination'})
    # print(pagination)
    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.find("span").string))
        # print(pages)
    # pages = pages[0:-1]
    # print(pages)
    max_page = pages[-1]
    return max_page


def extract_job(html):
#    titles = html.find_all("h2", {"class": "jobTitle"})
#    for title in titles:
#    job_title = title.find_all("span").get("title")
    job_title = html.find_all("span").get("title")
    if job_title is not None:
        print(job_title)
        return job_title


def extract_location(html):
    locations = html.find_all("div", {"class": "heading6"})
    for location in locations:
        job_location = location.find("span", {"class": "companyName"}).string
        if job_location is not None:
            return job_location


def extract_where(html):
    wheres = html.find_all("div", {"class": "heading6"})
    for where in wheres:
        job_where = where.find("div", {"class": "companyLocation"}).string
        if job_where is not None:
            return job_where


def extract_indeed_jobs(last_page):
    jobs = []
    # for page in range(last_page):
    result = requests.get(f'{URL}&start={last_page * LIMIT}')
    soup = BeautifulSoup(result.text, "html.parser")
    # results = soup.find_all("h2", {"class": "jobTitle"})
    results = soup.find_all("div", {"id": "mosaic-provider-jobcards"})
    print(results)
    print(results.find_all("span").get("title"))
    for result in results:
        job = {'job': extract_job(result), 'location': extract_location(result), 'where': extract_where(result)}
        jobs.append(job)
    return jobs

print(extract_indeed_jobs(0))