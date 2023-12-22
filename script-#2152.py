# coding: utf-8
#
import uiautomator2 as u2
import time

d = u2.connect()
d(text="Markor").click()
time.sleep(.5)
d.xpath('//*[@resource-id="net.gsantner.markor:id/nav_todo"]/android.widget.FrameLayout[1]').click()
time.sleep(.5)
d.drag(864,1920,0,1920)
time.sleep(.5)
d(description="当前日期").click()
time.sleep(.5)
d.xpath('//*[@resource-id="com.android.systemui:id/ends_group"]/android.widget.RelativeLayout[4]/android.widget.FrameLayout[1]').click()