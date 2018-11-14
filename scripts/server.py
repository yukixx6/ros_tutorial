#!/usr/bin/env python                                                           
import rospy
from std_srvs.srv import SetBool, SetBoolResponse

def callback_srv(data):
    resp = SetBoolResponse()
    resp.success = data.data
    if data.data == True:
        resp.message = "called"
    else:
        resp.message = "ready"
    print(resp.message)
    return resp

if __name__ == "__main__":
    rospy.init_node("srv_server")
    srv = rospy.Service('service_call', SetBool, callback_srv)
    rospy.spin()
