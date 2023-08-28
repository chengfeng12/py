# -*- encoding=utf8 -*-
__author__ = "nlsm"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

 
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["Android:///",])


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# script content
print("start...")
def V1():
    backIcon = Template(r"tpl1693203516621.png", record_pos=(-0.414, -0.765), resolution=(1080, 1920))
    buyIcon = Template(r"tpl1693203788487.png", record_pos=(0.138, 0.799), resolution=(1080, 1920))
    conformIcon = Template(r"tpl1693203935388.png", record_pos=(0.217, 0.797), resolution=(1080, 1920))
    subIcon = Template(r"tpl1693204011984.png", record_pos=(0.298, 0.8), resolution=(1080, 1920))
    cangIcon = Template(r"tpl1693205048880.png", record_pos=(-0.318, 0.215), resolution=(1080, 1920))
    num = 0

    def checkStatus():
        res = exists(buyIcon)
        if (res):
            touch(res)
            touch(cangIcon)
            touch(conformIcon)
            touch(subIcon)

    while (num < 1):
     checkStatus()
     num = num + 1
     sleep(0.01)
def v2():
    back = [76, 141]
#     点击进去详情
    touch([159, 879])
    sleep(0.8)
#    点击确定
    touch([637, 1824])
    sleep(0.5)
#    点击票档
    touch([205, 1192])
    sleep(0.5)
    #    点击确定
    touch([775, 1864])
    touch([824, 1815])
    touch([824, 1815])
    touch([824, 1815])
    touch([824, 1815])
    touch([824, 1815])
    touch([824, 1815])
    touch([824, 1815])
    touch([824, 1815])
    touch([824, 1815])
def v3():
    back = [76, 141]
#     点击进去详情
    num = 0
    while (num < 10):
        touch([659, 1818])
        touch([659, 1818])
        touch([659, 1818])
        touch([659, 1818])
        touch(back)
        num = num + 1
v3()
   
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)