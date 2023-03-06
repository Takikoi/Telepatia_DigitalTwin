import rospy
from control_msgs.msg import JointTrajectoryControllerState
from rospy_message_converter import json_message_converter
from ur10e_description import my_universal_robot as UR

PATH_TO_STREAM = 'src/ur10e_msgs_processor/stream/stream.json'

my_ur10e = UR.MyUniversalRobot()

def callback(data):
    rospy.loginfo(type(data))
    my_ur10e.set_joint_state(data)
    my_ur10e.update_stream(PATH_TO_STREAM)

def subscriber():
    rospy.init_node("ur10e_joint_state_reader" , anonymous=True)
    rospy.Subscriber("/eff_joint_traj_controller/state", JointTrajectoryControllerState, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        subscriber()
    except rospy.ROSInterruptException:
        pass