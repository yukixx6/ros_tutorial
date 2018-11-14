#!/usr/bin/env python                                                           
import rospy
from ros_tutorial.srv import DateTrigger, DateTriggerResponse
from datetime import datetime

def callback_srv(data):  #changed
    l = []
    d = DateTriggerResponse()                                                    
    d.date = ''
    d.time = ''
    try:
        now = datetime.now()
        l = str(now)

        for i in range(0,10):
            d.date += l[i]
        for i in range(11,25):
            d.time += l[i]
        d.date = int(d.date.replace('-', ''))
        d.time = float(d.time.replace(':',''))
        d.success = True
        return d
    except:
        d.success = False
        return d

if __name__ == '__main__':
    rospy.init_node('date_server')
    srv = rospy.Service('date_call', DateTrigger, callback_srv)
    rospy.spin()
