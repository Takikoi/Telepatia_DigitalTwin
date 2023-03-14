#!/bin/bash

source devel/setup.bash
roslaunch ur_robot_driver ur10e_bringup.launch robot_ip:=192.168.1.201 &
sleep 15s
roslaunch ur10e_moveit_config moveit_planning_execution.launch &
sleep 20s
roslaunch ur10e_moveit_config moveit_rviz.launch

