#!/usr/bin/env python
import rospy
from ros_tutorial.msg import Date  #changed

def callback(data):
    print("date : %d , time : %f" % (data.date,data.time) )  #changed

if __name__ == "__main__":
    rospy.init_node('time_sub')
    sub = rospy.Subscriber('Date_and_Time', Date , callback)  #changed
    rospy.spin()
