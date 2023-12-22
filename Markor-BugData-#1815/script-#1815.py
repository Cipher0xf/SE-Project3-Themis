# coding: utf-8
#
import uiautomator2 as u2
import time

d = u2.connect()
d(text="Markor").click()
time.sleep(.5)
d(description="更多选项").click()
time.sleep(.5)
d.xpath('//android.widget.ListView/android.widget.LinearLayout[2]').click()
time.sleep(.5)
d.xpath('//*[@resource-id="net.gsantner.markor:id/recycler_view"]/android.widget.LinearLayout[5]/android.widget.RelativeLayout[1]').click()
time.sleep(.5)
d.swipe_ext("up", scale=0.5)
time.sleep(.5)
d.xpath('//*[@resource-id="net.gsantner.markor:id/recycler_view"]/android.widget.LinearLayout[7]/android.widget.RelativeLayout[1]').click()