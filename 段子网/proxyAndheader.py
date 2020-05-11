import requests
import json
from random import choice
from lxml import etree

#读取ip
def getProxys():
    #打开代理文件
    f = open("ip.json",'r')
    #读取
    proxyStr = f.read()
    proxyArr = json.loads(proxyStr)
    #返回数组对象
    return proxyArr
#获取html


def getHtml(url,proxys):
    #user_agents
    USER_AGENTS = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
     ]
    #循环条件
    flag = True

    #循环请求，避免报错漏爬
    while flag:
        #捕获错误
        try:
            #获取随机proxy
            proxy = choice(proxys)
            
            #获取随机user-agene
            headers = {'User-Agent':choice(USER_AGENTS)}
            #发送请求
            rs = requests.get(url,headers=headers,proxies=proxy,timeout=3)
            #判断结果
            if rs.status_code == 200:
                #200 返回
                return rs.text
        #报错时跳过，继续请求
        except:
            continue
#提取内容
def getContent():
    #接收爬取页数
    page = int(input("输入抓取页数:"))
    #获取随机proxy
    proxys = getProxys()
    #请求地址
    url = "https://duanziwang.com/category/%E7%BB%8F%E5%85%B8%E6%AE%B5%E5%AD%90/"
    #输入抓取页数
    for i in range(1,page+1):
        #调用请求
        text = getHtml(url,proxys);
        #构建dom
        html = etree.HTML(text);
        #提取全部内容
        content = html.xpath("//article/div[@class='post-content']/p/text()")
        #输出全部内容
        for val in content:
            print(val)
        #下一页链接
        urlList = html.xpath("//nav[@class='pagination']/a[@class='next']/@href")
        #把结果转成字符串
        url = ''.join(urlList)

if __name__ == '__main__':
    getContent()
