import requests
from bs4 import BeautifulSoup
import time
import json
headers = {
    "Accept": "application/json",
    #"Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    #"Host": "www.google.com",
    "Host": "www.104.com.tw",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-5fbb6477-721f587d61090d9270800b75"
}


# url = 'https://www.104.com.tw/jobs/search/?jobsource=2018indexpoc&ro=0'
# url = 'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=%E7%A8%8B%E5%BC%8F%E8%A8%AD%E8%A8%88&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=14&asc=0&page={}&mode=s&jobsource=2018indexpoc'
# # url = 'https://www.google.com/search?q=%E8%A5%BF%E6%B4%8B%E6%A3%8B+%E6%88%B0%E8%A1%93&rlz=1C1CHBF_zh-TWTW923TW923&oq=%E8%A5%BF%E6%B4%8B&aqs=chrome.1.69i57j35i39j0i131i433l2j0i433l2j0i131i433j0.3806j0j7&sourceid=chrome&ie=UTF-8'
# ss = requests.session()
# # print(ss.cookies)
# for i in range(1,3):
#     url2= url.format(1)
#     req = ss.get(url2,headers=headers)
#     # print(req.text)
#     soup = BeautifulSoup(req.text,'html.parser')
#     titleTag = soup.select('article')
#     for i in titleTag[:-2]:
#         # print(i.attrs['data-job-no'])
#         # print(i.attrs,end='')
#         print('https:'+i.a.attrs['href'])
#         # time.sleep(1)
#         req1 = ss.get('https:' + i.a.attrs['href'])
#         soup1 = BeautifulSoup(req1.text,'html.parser')
#         print(soup1)
#         break

# BeautifulSoup(我們拿到的文字,我們要的格式)
url = 'https://www.104.com.tw/jobs/search/?jobsource=2018indexpoc&ro=0'
url = 'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=%E7%A8%8B%E5%BC%8F%E8%A8%AD%E8%A8%88&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=14&asc=0&page={}&mode=s&jobsource=2018indexpoc'
url3 ='https://www.104.com.tw/jobs/search/list?ro=0&kwop=7&keyword=%E7%A8%8B%E5%BC%8F%E8%A8%AD%E8%A8%88&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=14&asc=0&page={}&mode=s&jobsource=2018indexpoc'
ss = requests.session()
for i in range(1, 4):
    url2 = url.format(1)
    ss.headers.update(headers)
    req = ss.get(url2)
    # print(req.text)
    if i == 1:
        soup = BeautifulSoup(req.text, 'html.parser')
    else:
        # soup = json.loads(req.text,encoding='UTF-8')
        soup = json.JSONDecoder().decode(req.text)

    # titleTag = soup.select('article')
    # print(soup)
    # print(type(soup))
    if i != 1:
            print(soup['data']['list'])
    # for j in titleTag[:-2]:
    #     print('https:' + j.a.attrs['href'])
    #     # req1 = ss.get('https:' + i.a.attrs['href'])
    #     # soup1 = BeautifulSoup(req1.text,'html.parser')
    #     # print(soup1)
    #     break
    # print(ss.cookies)
    headers[
        "Referer"] = "https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=%E7%A8%8B%E5%BC%8F%E8%A8%AD%E8%A8%88&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=14&asc=0&page={}&mode=s&jobsource=2018indexpoc".format(
        i)
    headers["Connection"] = "keep-alive"
    url = url3


