from tools import config
from tools.read_json import ReadJson


class PostParameter:

    def post_param(self,port,filename,case_number):
        url = config.DevConfig.url + ReadJson(port, filename).read_json()["api"]
        headers = ReadJson(port, "header.json").read_json()
        common_param = ReadJson(port, "common_param.json").read_json()
        data = ReadJson(port, filename).read_json()["interface"][case_number]["params"]
        expect_results = ReadJson(port, filename).read_json()["interface"][case_number]["assert"]
        arrs = {}
        arrs["url"] = url
        arrs["headers"] = headers
        arrs["common_param"] = common_param
        arrs["data"] = data
        arrs["expect_results"] = expect_results
        return arrs

if __name__ == '__main__':
    param = PostParameter().post_param("shop","login.json", "case002")
    print(param["expect_results"])