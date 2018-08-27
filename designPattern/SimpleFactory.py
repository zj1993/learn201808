# -*- coding: utf-8 -*-
class Man:
    def __init__(self, sex):
        self.sex = sex

    def say(self):
        return self.sex


class Woman:
    def __init__(self, sex):
        self.sex = sex

    def say(self):
        return self.sex


class UnknowSex:
    def say(self):
        return '操作错误！'


class Factory:
    def __init__(self, sex):
        self.sex = sex

    def get_say(self):
        if self.sex == '男人':
            return Man(self.sex)

        elif self.sex == '女人':
            return Woman(self.sex)
        else:
            return UnknowSex()


def test_fac():
    sex = input('请输入性别：')
    fac = Factory(sex)
    get_say = fac.get_say()
    say = get_say.say()
    print(say)


test_fac()