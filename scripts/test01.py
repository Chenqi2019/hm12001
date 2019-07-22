import allure
import pytest


class Test01():
    @allure.step(title="正在执行登录操作")
    def test001(self):
        print("test001被执行")

    @allure.step(title="正在执行退出操作")
    def test002(self):
        print("test002被执行")


    def test003(self):
        allure.attach("描述：", "正在执行该操作")
        print("test003被执行")

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test004(self):
        allure.attach("描述：", "")
        print("test004被执行")

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test005(self):
        # with open("./picture/cookie产生及应用草图.jpg","rb")as f:
        #     allure.attach("测试成功：",f.read(),allure.attach_type.JPG)
        allure.attach("描述：","")
        assert 0
        print("test005被执行")