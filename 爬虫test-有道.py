
# -*- coding:utf-8 -*-
'''
 使用 POST 方式抓取 有道翻译
    urllib2.Request(requestURL, data=data, headers=headerData)
    Request 方法中的 data 参数不为空，则默认是 POST 请求方式
    如果 data 为空则是 Get 请求方式
    {"errorCode":50}错误：
         有道翻译做了一个反爬虫机制，就是在参数中添加了 salt 和 sign 验证，具体操作说明参考：
         http://www.tendcode.com/article/youdao-spider/
'''
import urllib.parse
import urllib.request
import json
import time

while True:
    content = input('请输入需要翻译的词语(按0退出)：')
    if(content=="0"):
        break;

    # url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    head = {}
    head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'

    data = {}
    data['i']=content
    data['doctype']='json'
    data['keyfrom']='fanyi.web'
    data['typoResult']='true'
    data['from']='AUTO'
    data['to']='AUTO'
    data['smartresult']='dict'
    data['client']='fanyideskweb'
    data['salt']='1520416292076'
    data['sign']='41fe7ea28425a0a4ceb88ab4c8609d13'
    data['version']='2.1'

    data['action']='FY_BY_CLICKBUTTION'
    data['typoResult']='false'
    # 编码
    data = urllib.parse.urlencode(data).encode('utf-8')
    
    # 发送请求，带data就是post，不带data是get
    #response = urllib.request.urlopen(url,data) #不添加heades防检测
    req = urllib.request.Request(url,data,head) #加入header（必须为字典）防止被检测出爬虫
    response = urllib.request.urlopen(req)
    '''
    #通过add_header()添加
    req = urllib.request.Request(url,data)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36')
    response = urllib.request.urlopen(req)
    '''
    # 解码
    html = response.read().decode('utf-8')
    ta = json.loads(html)  # json.loads()用于将str类型的数据转成dict。参考 Json模块
    print("结果为："+ta['translateResult'][0][0]['tgt'])

    time.sleep(2)

