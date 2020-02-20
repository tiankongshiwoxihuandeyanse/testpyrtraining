import unittest
from tools.read_json import ReadJson


class ReadParameterized(object):
    # @parameterized.expand(read_params())
    # def test_parameterized(self,case_number):
    #     data = read_json.ReadJson("login.json").read_json()["interface"][case_number]["params"]
    def __init__(self,port,filename):
        self.port = port
        self.filename = filename

    def read_parameterized(self):
        data = ReadJson(self.port,self.filename).read_json()["interface"]
        # print(data)
        arrs = []
        for i in data.values():
            # print(i["params"])
            arrs.append((
                i["params"].get('account'),
                i["params"].get('password')
            ))
        # print(arrs)
        return arrs

    def read_params(self):
        data = ReadJson(self.port,self.filename).read_json()["interface"]
        print(data)
        arrs = []
        for i in data.keys():
            print(i)
            arrs.append((i))
        print(arrs)
        return arrs


if __name__ == '__main__':
    ReadParameterized("shop","login.json").read_params()

