import requests
from tools.change_json_value import get_new_json, rewrite_json_file

class Api_Login(object):
    def __init__(self):
        pass

    def login (self,url,headers,common_param,data,expect_results):
        # url = "https://dev-fitback.dealsports.cn/shop/login/"
        # headers = {"Content_Type":"application/json"}
        # common_param = {"app_channel":"应用宝","app_version":"1.7.0","os_type":1,"os_version":1,"device_uuid":1}
        # data = {"account":"18706174433","password":"a123456"}
        data.update(common_param)
        r = requests.post(url,headers = headers,json=data)
        # print("响应时间：",r.elapsed.total_seconds()).encode('raw_unicode_escape')
        print("接口响应："+r.content.decode('unicode_escape'))

        if r.json()["code"] == 0:
            token = r.json()['data']['token']
            # print(token)
            m_json_data = get_new_json("../../date/"+"shop/"+"header.json", "token", token)
            rewrite_json_file("../../date/"+"shop/"+"header.json", m_json_data)
        else:
            pass
        return r


