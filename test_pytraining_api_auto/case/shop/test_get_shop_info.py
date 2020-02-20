from api.shop.api_get_shop_info import Api_GetShopInfo
import unittest
from tools.post_param import PostParameter
from tools.read_parameterized import ReadParameterized
from parameterized import parameterized
from case.shop.shop_login import Login
# from pathlib import Path
# import warnings
# warnings.filterwarnings('ignore')
#
# # 获取当前文件名称：eg test_get_shop_info.py
# filename = Path(__file__).stem
#
# # 获取当前文件名称：eg test_get_shop_info.py文件就会 变成name=get_shop_info
# api_name = Path(__file__).stem[5:]

# Login().test_shop_login()


class TestGetShopInfo(unittest.TestCase):
    # @classmethod
    # def setUp(self):
    #     pass
    #
    # @classmethod
    # def tearDown(self):
    #     pass

    @parameterized.expand(ReadParameterized("shop","get_shop_info.json").read_params())
    def test_get_shop_info(self,case_number):

        param = PostParameter().post_param("shop","get_shop_info.json",case_number)

        r = Api_GetShopInfo().get_shop_info(param["url"],param["headers"],param["common_param"],param["data"],param["expect_results"])

        self.assertEqual(param["expect_results"]["code"],r.json()["code"])
        self.assertEqual(param["expect_results"]["msg"], r.json()["msg"])

if __name__ == '__main__':
    unittest.main()