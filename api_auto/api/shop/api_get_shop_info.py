import requests
class Api_GetShopInfo(object):
    def __init__(self):
        pass
    def get_shop_info(self,url,headers,common_param,data,expect_results):
        # url = "https://dev-fitback.dealsports.cn/shop/login/"
        # headers = {"Content_Type":"application/json"}
        # common_param = {"app_channel":"应用宝","app_version":"1.7.0","os_type":1,"os_version":1,"device_uuid":1}
        # data = {"account":"18706174433","password":"a123456"}
        data.update(common_param)
        r = requests.post(url,headers = headers,json=data)
        #print("响应时间：",r.elapsed.total_seconds())
        print("接口响应："+r.content.decode('unicode_escape'))
        return r


