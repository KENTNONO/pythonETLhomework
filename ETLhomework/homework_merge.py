import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
headers = {
    "Accept": "application/json",
    "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Host": "www.104.com.tw",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-5fbb6477-721f587d61090d9270800b75"
}
# 做
def returnListAns(keyword):
    url = "https://www.104.com.tw/job/{}?jobsource=hotjob_chr".format(keyword)
    headers['Referer']=url
    ss.headers.update(headers)
    url2 = "https://www.104.com.tw/job/ajax/content/{}".format(keyword)
    req = ss.get(url2)
    output = json.JSONDecoder().decode(req.text)
    specialList = []
    for i in output['data']['condition']['specialty']:
        specialList.append(i['description'].upper())
    return {'special':specialList,'contact':output['data']['contact'],'welfare':output['data']['welfare']};



listans = {}
ans = []
url = 'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=%E7%A8%8B%E5%BC%8F%E8%A8%AD%E8%A8%88&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=14&asc=0&page=1&mode=s&jobsource=2018indexpoc'
ss = requests.session()
ss.headers.update(headers)
req = ss.get(url)
soup = BeautifulSoup(req.text,'html.parser')
titleTag = soup.select('article')
for i in titleTag[:-2]:
    listans['jobName'] = i.get('data-job-name')
    listans['custName'] = i.get('data-cust-name')
    listans['info'] = i.find('p').getText().replace('\r',' ').replace('\n',' ').replace('\t',' ').replace(',',' ')
    keyword = i.a.get('href')[21:i.a.get('href').index('?')]
    listans.update(returnListAns(keyword))
    ans.append(listans)
    listans = dict()
url ='https://www.104.com.tw/jobs/search/list?' \
     'ro=0&kwop=7&keyword=%E7%A8%8B%E5%BC%8F%E8%A8%AD%E8%A8%88&' \
     'expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&' \
     'order=14&asc=0&page={}&mode=s&jobsource=2018indexpoc'

# for i in range(2,4):
#     j = i - 1
#     headers["Referer"]="https://www.104.com.tw/jobs/search/?ro=0&kwop=7" \
#                        "&keyword=%E7%A8%8B%E5%BC%8F%E8%A8%AD%E8%A8%88&" \
#                        "expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&" \
#                        "order=14&asc=0&page={}&mode=s&jobsource=2018indexpoc".format(j)
#     ss.headers.update(headers)
#     req = ss.get(url.format(i))
#     soup = json.JSONDecoder().decode(req.text).get('data').get('list')
#     print(soup)
#     for j in range(len(soup)):
#         listans['jobName'] = soup[j].get('jobName')
#         listans['custName'] = soup[j].get('custNameRaw')
#         listans['info'] = soup[j].get('description').replace('\r', ' ').replace('\n', ' ').replace('\t', ' ').replace(',',' ')
#         keyword = soup[j].get('link').get('job')[21:soup[j].get('link').get('job').index('?')]
#         listans.update(returnListAns(keyword))
#         ans.append(listans)
#         listans=dict()

print(ans)
listSpecial = ['JAVA','PYTHON','C','C#']
df = pd.DataFrame(columns=['Job_company','Job Openings','ob_content','ob_welfare','ob_cotact']+listSpecial)
for i in range(len(ans)):
    lanList = []
    for j in listSpecial:
        lanList.append(1 if j in ans[i]['special'] else 0)
    df.loc[i]=[ans[i]['custName'], ans[i]['jobName'], ans[i]['info'], ans[i]['welfare']['welfare']
        , ans[i]['contact']['hrName']]+lanList
print(df)
df.to_csv(r'./test_pandas.csv',index=False,encoding='utf-8')
