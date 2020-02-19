import sys
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)
from api.shop.api_login import Api_Login
from tools.post_param import PostParameter
from tools.read_parameterized import ReadParameterized
from parameterized import parameterized
from case.shop.shop_login import Login
from pathlib import Path
import warnings,unittest
warnings.filterwarnings('ignore')
import os

print("os.path.abspath(__file__) = ", os.path.abspath(__file__))
print("os.path.realpath(__file__) = ", os.path.realpath(__file__))
# 获取当前文件名称：eg test_get_shop_info.py
filename = Path(__file__).stem

# 获取当前文件名称：eg test_get_shop_info.py文件就会 变成name=get_shop_info
api_name = Path(__file__).stem[5:]

Login().test_shop_login()


class Login(unittest.TestCase):
    @classmethod
    def setUp(self):
        pass

    @classmethod
    def tearDown(self):
        pass

    @parameterized.expand(ReadParameterized("shop","login.json").read_params())
    def test_shop_login(self,case_number):

        param = PostParameter().post_param("shop","login.json",case_number)

        r = Api_Login().login(param["url"],param["headers"],param["common_param"],param["data"],param["expect_results"])

        self.assertEqual(param["expect_results"]["code"],r.json()["code"])
        self.assertEqual(param["expect_results"]["msg"], r.json()["msg"])

if __name__ == '__main__':
    unittest.main()