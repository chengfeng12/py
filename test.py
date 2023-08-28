# -*- encoding=utf8 -*-
__author__ = "nlsm"
from multiprocessing import Pool,Manager
import unittest
from airtest.core.api import *
from airtest.cli.parser import cli_setup
# airtest 获取当前屏幕分辨率
def info(po):
    width = G.DEVICE.display_info['width']
    height = G.DEVICE.display_info['height']
    print(width,height)
#     已知相对坐标,转换成绝对坐标
    x1 = po[0]*width
    y1 = po[1]*height
#     已知绝对坐标[88.1060],转换成相对坐标
    x2 = 88/width
    y2 = 1060/height
    poco.click([x2,y2])
    return [x2,y2]
# info([0.5, 0.5])
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/emulator-5554?cap_method=JAVACAP&ori_method=ADBORI&touch_method=MINITOUCH&",])


#安卓实例
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
#poco实例化
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

    
#!/usr/bin/python3
 
# script content
print("start...")
#  收集金币
jbIcon = Template(r"tpl1692863394680.png", record_pos=(-0.08, 0.007), resolution=(1920, 1080))
#  收集玉米
ymIcon = Template(r"tpl1692861597137.png", record_pos=(0.008, 0.076), resolution=(1920, 1080))
#  收集木头
mtIcon = Template(r"tpl1692861600270.png", record_pos=(0.087, 0.134), resolution=(1920, 1080))
#  收集石头
stIcon = Template(r"tpl1692861603435.png", record_pos=(0.176, 0.197), resolution=(1920, 1080))
#  收集资源

def sjzy(zyIcon, msg):
    print("cjzy...");
    assert_not_equal(True, assert_exists(zyIcon, "是否有" + msg), msg + "条件成立");
    touch(zyIcon);
    return
# 开始收集
def start_sj():
    sjzy(jbIcon, "金币");
    sjzy(ymIcon, "玉米");
    sjzy(mtIcon, "木头");
    sjzy(stIcon, "石头");

def start_cj():
    out = Template(r"tpl1692866393311.png", record_pos=(-0.451, 0.23), resolution=(1920, 1080))
    touch(out)
# 野外采集
def ywcj():
    #     搜索资源
    searchIcon = Template(r"tpl1692870349735.png", record_pos=(-0.45, 0.14), resolution=(1920, 1080))
    touch(searchIcon)
    Template(r"tpl1693211835567.png", record_pos=(-0.007, -0.047), resolution=(1920, 1080))
    Template(r"tpl1693211847412.png", record_pos=(-0.009, -0.155), resolution=(1920, 1080))
    Template(r"tpl1693211854104.png", record_pos=(-0.11, -0.115), resolution=(1920, 1080))
    Template(r"tpl1693211957151.png", record_pos=(-0.028, 0.051), resolution=(1920, 1080))
    Template(r"tpl1693211974265.png", record_pos=(-0.094, -0.008), resolution=(1920, 1080))
    Template(r"tpl1693212017912.png", record_pos=(-0.004, 0.015), resolution=(1920, 1080))
    level = 6
    

zyIcons = {
  "ym": {
      "4": Template(r"tpl1693211760536.png", record_pos=(0.081, 0.109), resolution=(1920, 1080)),
      "5": Template(r"tpl1693211784993.png", record_pos=(-0.002, -0.002), resolution=(1920, 1080)),
      "6": Template(r"tpl1693211816293.png", record_pos=(-0.002, -0.001), resolution=(1920, 1080))
    },
    "mt": {
      "4": Template(r"tpl1693211854104.png", record_pos=(-0.11, -0.115), resolution=(1920, 1080)),
      "5": Template(r"tpl1693212017912.png", record_pos=(-0.004, 0.015), resolution=(1920, 1080)),
      "6": Template(r"tpl1693211974265.png", record_pos=(-0.094, -0.008), resolution=(1920, 1080))
    }
}
#     采集玉米
cjymIcon = Template(r"tpl1692871400008.png", record_pos=(-0.149, 0.203), resolution=(1920, 1080))
cjymIconD = Template(r"tpl1692875067954.png", record_pos=(-0.083, 0.031), resolution=(1920, 1080))
#     采集木头
cjmtIcon = Template(r"tpl1692871256286.png", record_pos=(0.003, 0.216), resolution=(1920, 1080))
cjmtIconD = Template(r"tpl1692875098122.png", record_pos=(0.118, 0.022), resolution=(1920, 1080))
#     采集石头
cjstIcon = Template(r"tpl1692871395605.png", record_pos=(0.155, 0.214), resolution=(1920, 1080))
cjstIconD = Template(r"tpl1692875116820.png", record_pos=(0.004, 0.016), resolution=(1920, 1080))
#     采集金币
cjjbIcon = Template(r"tpl1692871417958.png", record_pos=(0.305, 0.217), resolution=(1920, 1080))
cjjbIconD = Template(r"tpl1692875153721.png", record_pos=(0.003, -0.014), resolution=(1920, 1080))
level = 0
def cjzy(el, elD):
    start_cj();
    ywcj()
    sleep(1.0)
    touch(el)
    sleep(1.0)
    check_level();
    search_zy(el, elD)
    
def cjzy_rep(el, elD):
#     searchIcon = Template(r"tpl1692870349735.png", record_pos=(-0.45, 0.14), resolution=(1920, 1080))
#     touch(searchIcon)
    ywcj()
    sleep(1.0)
    touch(el)
    sleep(1.0)
    check_level();
    search_zy(el, elD)
    
# 搜索资源
searchNumber = 0;
# 采集队列数
cjNumber = 0

# searchEl, zyKey
def search_zy(searchEl, zyKey):
    sleep(3.0)
#     touch(Template(r"tpl1692872515044.png", record_pos=(0.304, 0.099), resolution=(1920, 1080)))
#     touch(searchEl)
#     result = assert_exists(Template(r"tpl1692872625851.png", record_pos=(-0.0, -0.079), resolution=(1920, 1080)), "资源搜索成功")
    result = assert_exists(zyIcons[zyKey][str(level)], "资源搜索成功")
    sleep(3.0)
    global searchNumber
    global cjNumber

    if result:
        searchNumber = 0;
        #  点击资源
        touch([965, 545])
        sleep(1.0)
        cjBtn = assert_exists(Template(r"tpl1692875581926.png", record_pos=(0.244, 0.096), resolution=(1920, 1080)), "点击了采集")
        touch(cjBtn);
        sleep(1.0)
        setBudui = assert_exists(Template(r"tpl1692875692811.png", record_pos=(0.292, -0.171), resolution=(1920, 1080)), "点击了设置部队")
        touch(setBudui)
        sleep(1.0)
        moveBudui = assert_exists(Template(r"tpl1692875887971.png", record_pos=(0.236, 0.201), resolution=(1920, 1080)), "开始移动部队")
        touch(moveBudui);
        sleep(1.0)
        #  开始下一轮的搜索资源
        if (cjNumber < 5):
           cjNumber = cjNumber + 1;
           cjzy_rep(searchEl, zyKey)
        else:
            cjNumber = 0

    elif (searchNumber < 10):
        print("循环了")
        searchNumber = searchNumber + 1;
        reduce_level()
        search_zy(searchEl, zyKey)
    else:
        searchNumber = 0

#  控制采集资源等级
def check_level():
    num = 0
    while (num < 5):
        num = num + 1;
        add_level()
# 加资源等级      
def add_level():
    global level
    addIcon = Template(r"tpl1692870422118.png", record_pos=(-0.179, 0.036), resolution=(1920, 1080))
    touch(addIcon);
    if (level < 6):
        level = level + 1
# 减资源等级 
def reduce_level():
    global level
    reduceIcon = Template(r"tpl1692870487933.png", record_pos=(-0.394, 0.036), resolution=(1920, 1080))
    touch(reduceIcon);
    if (level > 4):
        level = level - 1

    

# touch(Template(r"tpl1692861629499.png", record_pos=(0.457, 0.243), resolution=(1920, 1080)))
# touch(Template(r"tpl1692861696625.png", record_pos=(0.306, 0.251), resolution=(1920, 1080)))
# touch(Template(r"tpl1692861710486.png", record_pos=(0.09, 0.17), resolution=(1920, 1080)))
def privilege():
    touch(Template(r"tpl1692862345201.png", record_pos=(-0.398, -0.232), resolution=(1920, 1080)))
    sleep(1.0)
    touch([1522, 262], 2)
    sleep(2.0)
    touch([1182, 601], 2)
    touch(Template(r"tpl1693209031958.png", record_pos=(0.353, -0.221), resolution=(1920, 1080)))
isFirst = True
def start_game():
    if isFirst:
        print("test")
        touch(Template(r"tpl1692948788987.png", record_pos=(0.116, -0.521), resolution=(1080, 1920)))
        sleep(30.0)   
    loginIcon = assert_exists(Template(r"tpl1692947722412.png", record_pos=(0.008, 0.188), resolution=(1920, 1080)), "点击登录")
    touch(loginIcon);
    sleep(30.0)   
    is_first = False
    privilege()
    sleep(1.0)
    start_sj()
# start_game()
cjzy(cjymIcon, 'ym')
# start_sj()
def switch_account():
    print(1)
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)



