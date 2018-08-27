# -*- coding: utf-8 -*-

class Ps2(object):
    def Ps2(self):
        print('ps2接口')

class Usb(object):
    def Usb(self):
        print('usb接口')

class Adapter(Ps2):
    def __init__(self):
        self.Usb = Usb()

    def request(self):
        self.Usb.Usb()

if __name__ == "__main__":
    Usb = Adapter()
    Usb.request()