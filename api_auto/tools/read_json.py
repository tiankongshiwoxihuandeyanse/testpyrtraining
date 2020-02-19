import json


class ReadJson:
    def __init__(self, port,filename):
        # self.dir = "../date/shop/"+ filename
        # self.filepath = self.dir + '\\'  + port + '\\' + filename
        self.filepath = "../../date/" + port + '/' +  filename

    def read_json(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            # print(json.load(f))
            print(self.filepath)
            return json.load(f)


if __name__ == '__main__':
    # case_represent = ReadJson("login.json").read_json()["case_ represent"]
    login_001 = ReadJson("shop","login.json").read_json()["interface"]["case001"]["params"]

    print(login_001)