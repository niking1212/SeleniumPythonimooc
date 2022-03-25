# coding=utf-8
import unittest


class FirstCase02(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("所有case执行之前的前置")

    @classmethod
    def tearDownClass(cls) -> None:
        print("所有case执行之前的后置")

    def setUp(self):
        print("这个是case的前置条件")

    def tearDown(self):
        print("这个是case的后置条件")

    # @unittest.skip # 不执行第一条
    def test_first001(self):
        print("这是第01条case")

    def test_first002(self):
        print("这是第02条case")


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(FirstCase02('test_first02'))
    suite.addTest(FirstCase02('test_first01'))
    unittest.TextTestRunner().run(suite)
