from parameterized import parameterized

from api.shop.api_login import Api_Login
import unittest

from tools import read_parameterized
from tools.post_param import PostParameter


class Login:
    # @parameterized.expand(read_parameterized.ReadParameterized("shop","login.json").read_params())
    def test_shop_login(self,case_number = "case001"):
        param = PostParameter().post_param("shop","login.json", "case002")
        r = Api_Login().login(param["url"], param["headers"], param["common_param"], param["data"],
                              param["expect_results"])

        # self.assertEqual(param["expect_results"]["code"],r.json()["code"])
        # self.assertEqual(param["expect_results"]["msg"], r.json()["msg"])


if __name__ == '__main__':
    Login().test_shop_login("case002")
