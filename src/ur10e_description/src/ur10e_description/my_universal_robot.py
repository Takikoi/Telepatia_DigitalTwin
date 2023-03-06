import rospy
import json
import os
import io
from rospy_message_converter import json_message_converter
from rospy_message_converter import message_converter
# import prett

class MyUniversalRobot:
    
    joint_state = ''

    def __init__(self) -> None:
        pass

    def set_joint_state(self, msgs):
        # self.joint_state = json_message_converter.convert_ros_message_to_json(msgs)
        self.joint_state = message_converter.convert_ros_message_to_dictionary(msgs)

    def update_stream(self, stream_file_path):
            # checks if file exists
        if os.path.isfile(stream_file_path) and os.access(stream_file_path, os.R_OK):
            print ("File exists and is readable")
        else:
            print ("Either file is missing or is not readable, creating file...")
        
        with io.open(stream_file_path, 'w') as f:
            f.write(json.dumps(self.joint_state, indent=2))