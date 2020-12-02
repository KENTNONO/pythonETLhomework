import requests
from bs4 import BeautifulSoup
import json

headers = {
    "Accept": "application/json, text/plain, */*",
    #"Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    #"Host": "www.google.com",
    # "Host": "www.104.com.tw",
    "Referer": "https://www.104.com.tw/job/745ak?jobsource=hotjob_chr",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-5fbb6477-721f587d61090d9270800b75"
}


url = 'https://www.104.com.tw/jobs/search/?jobsource=2018indexpoc&ro=0'
url = 'https://www.104.com.tw/job/ajax/content/745ak'
#url = 'https://www.google.com/search?q=%E8%A5%BF%E6%B4%8B%E6%A3%8B+%E6%88%B0%E8%A1%93&rlz=1C1CHBF_zh-TWTW923TW923&oq=%E8%A5%BF%E6%B4%8B&aqs=chrome.1.69i57j35i39j0i131i433l2j0i433l2j0i131i433j0.3806j0j7&sourceid=chrome&ie=UTF-8'
# ss = requests.session()
#print(ss.cookies)
req = requests.get(url,headers=headers)
# req = ss.get(url,headers=headers)
# print(req.text)
# print(json.loads(req.text,encoding='utf-8'))
print(json.JSONDecoder().decode(req.text))
# soup = BeautifulSoup(req.text,' html.parser')
# titleTag = soup.select('article')
# for i in titleTag[:-2]:
#     # print(i.attrs['data-job-no'])
#     print(i.attrs,end='')
#     print(i.a.attrs['href'])
# BeautifulSoup(我們拿到的文字,我們要的格式)