# -*- coding: utf-8 -*-

class Human:
    def say(self):
        pass

class Man(Human):
    def say(self):
        print('男人')

class Woman(Human):
    def say(self):
        print('女人')

class AbstractFactory:
    def creatMan(self):
        pass

class ManFactory(AbstractFactory):
    def creatMan(self):
        return Man()

class WomanFactory(AbstractFactory):
    def creatMan(self):
        return Woman()

if __name__ == "__main__":
    testFactory = ''
    sex = input('请输入性别：')
    if sex == '男人':
        testFactory = ManFactory()
    elif sex == '女人':
        testFactory = WomanFactory()
    else:
        print('操作错误')
        exit(0)

    sextest = testFactory.creatMan()
    sextest.say()
