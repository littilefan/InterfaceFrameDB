# 2020-6-7
import requests
import json

class HttpClient(object):
    def __init__(self):
        pass

    def request(self,requestUrl,requestMethod,paramsType,requestData,headers = None,cookies = None):
        # 处理http请求,包括get、post
        if requestMethod.lower() == "post":
            if paramsType == "form":
                response = self.__post(requestUrl, data=json.dumps(requestData),headers = headers)
                return response
            elif paramsType == "json":
                response = self.__post(requestUrl, json=json.dumps(requestData),headers = headers)
                return response
        elif requestMethod.lower() == "get":
            if paramsType == "url":
                requestUrl = "url:%s,data:%s" %(requestUrl,requestData)
                response = self.__get(requestUrl,headers = headers,cookies = cookies)
                return response
            elif paramsType == "params": # 较少用
                response = self.__get(requestUrl,requestData,headers = headers,cookies = cookies)
                return response
        elif requestMethod.lower() == "put/delete/head":
            pass

    # 私有方法,不允许其他调用
    def __post(self,url,data = None,json = None,**kwargs):
        # 处理post类各种情况的请求,data接收表单
        response = requests.post(url,data = data,json = json,**kwargs)
        return response

    # 私有方法
    def __get(self,url,params = None,**kwargs):
        # 处理get类各种情况的请求
        response = requests.get(url,params = params,**kwargs)
        return response

if __name__ == '__main__':
    hc = HttpClient()
    res = hc.request("http://39.106.41.11:8080/register/","post",
               "form",
               {"username":"lilysse342","password":"lily12323","email":"lily@qq.com"}
            )
    print(res.status_code)
    print(res.json())
