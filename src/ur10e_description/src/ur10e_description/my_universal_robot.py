import rospy
import json
import os
import io
from rospy_message_converter import json_message_converter
from rospy_message_converter import message_converter
# import prett

class MyUniversalRobot:
    
    joint_state = {}
    wrench_state = {}

    def __init__(self) -> None:
        pass

    def set_joint_state(self, msgs):
        self.joint_state = message_converter.convert_ros_message_to_dictionary(msgs)

    def update_joint_stream(self, stream_file_path):
        with io.open(stream_file_path, 'w') as f:
            f.write(json.dumps(self.joint_state, indent=2))

    def set_wrench_state(self, msgs):
        self.wrench_state = message_converter.convert_ros_message_to_dictionary(msgs)

    def update_wrench_stream(self, stream_file_path):
        with io.open(stream_file_path, 'w') as f:
            f.write(json.dumps(self.wrench_state["wrench"], indent=2))