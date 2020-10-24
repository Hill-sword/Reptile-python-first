import os

import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    if not os.path.exists("./SanGou"):
        os.mkdir("./SanGou")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.37 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }
    url ="https://www.shicimingju.com/book/sanguoyanyi.html"
    reponse = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(reponse.text, "lxml")
    list_div = soup.select("div .book-mulu a")
    dict_a = dict()
    for i in list_div:
        if i['href'][-5:] == '.html':
            dict_a.update({i['href']: i.string})
    fp = open("./SanGou/三国.txt", 'w', encoding="utf-8")
    for i in dict_a.items():
        url = "https://www.shicimingju.com"
        # 先访问到该链接
        file_name =i[1][1:-2]+'.txt'
        url += i[0]
        respon = requests.get(url=url, headers=headers, timeout=10)
        soup1 = BeautifulSoup(respon.text, "lxml")
        text_main = soup1.find("div", class_="chapter_content").text
        with open("./SanGou/"+file_name,'w',encoding="utf-8") as fp:
            fp.write(text_main)
        print(i[1], "下载成功！！")



