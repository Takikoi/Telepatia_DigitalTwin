import rospy
from control_msgs.msg import JointTrajectoryControllerState
from geometry_msgs.msg import Wrench
from rospy_message_converter import json_message_converter
from ur10e_description import my_universal_robot as UR

PATH_TO_JOINT_STREAM = 'src/ur10e_msgs_processor/stream/stream_joint.json'
PATH_TO_WRENCH_STREAM = 'src/ur10e_msgs_processor/stream/stream_wrench.json'

my_ur10e = UR.MyUniversalRobot()

def callback_pos(data):
    my_ur10e.set_joint_state(data)
    my_ur10e.update_joint_stream(PATH_TO_JOINT_STREAM)

def callback_wrench(data):
    my_ur10e.set_wrench_state(data)
    my_ur10e.update_wrench_stream(PATH_TO_WRENCH_STREAM)

def subscriber():
    rospy.init_node("ur10e_joint_state_reader" , anonymous=True)
    rospy.Subscriber("/scaled_pos_joint_traj_controller/state", JointTrajectoryControllerState, callback_pos)
    rospy.Subscriber("/wrench", Wrench, callback_wrench)
    rospy.spin()

if __name__ == '__main__':
    try:
        subscriber()
    except rospy.ROSInterruptException:
        pass