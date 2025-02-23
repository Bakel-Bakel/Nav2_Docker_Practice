#!/usr/bin/env python3
import rclpy
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped
import tf_transformations

def create_pose_stamped(navigator, position_x, position_y, orientation_z):
	q_x, q_y, q_z, q_w = tf_transformations.quaternion_from_euler(0.0, 0.0, orientation)
	pose = PoseStamped()
	pose.header.frame_id = 'map'
	pose.header.stamp = navigator.get_clock().now().to_msg()
	pose.pose.position.x = position_x
	pose.pose.position.y = position_y
	pose.pose.position.z = 0.0
	pose.pose.orientation.x = q_x
	pose.pose.orientation.y = q_y
	pose.pose.orientation.z = q_z
	pose.pose.orientation.w = q_w
	return pose

def main():
	rclpy.init()
	nav = BasicNavigator()
	
	
	#Set initial pose
	q_x, q_y, q_z, q_w = tf_transformations.quaternion_from_euler(0.0, 0.0, 0.0)
	initial_pose = PoseStamped()
	initial_pose.header.frame_id = 'map'
	initial_pose.header.stamp = nav.get_clock().now().to_msg()
	initial_pose.pose.position.x = 0.0
	initial_pose.pose.position.y = 0.0
	initial_pose.pose.position.z = 0.0
	initial_pose.pose.orientation.x = q_x
	initial_pose.pose.orientation.y = q_y
	initial_pose.pose.orientation.z = q_z
	initial_pose.pose.orientation.w = q_w
	nav.setInitialPose(initial_pose)
	
	#wait for Nav2
	nav.waitUntilNav2Active()
	
	q_x, q_y, q_z, q_w = tf_transformations.quaternion_from_euler(0.0, 0.0, 0.0)
	goal_pose = PoseStamped()
	goal_pose.header.frame_id = 'map'
	goal_pose.header.stamp = nav.get_clock().now().to_msg()
	goal_pose.pose.position.x = 3.8
	goal_pose.pose.position.y = 3.5
	goal_pose.pose.position.z = 0.0
	goal_pose.pose.orientation.x = q_x
	goal_pose.pose.orientation.y = q_y
	goal_pose.pose.orientation.z = q_z
	goal_pose.pose.orientation.w = q_w
	
	nav.goToPose(goal_pose)
	while not nav.isTaskComplete():
		feedback = nav.getFeedback()
		print(feedback)
		
	print(nav.getResult(), " Done with inital motion, proceeding to waypoint task")
	
	point1 = create_pose_stamped(nav,1.5 ,5.5 ,3.14 )
	point2 = create_pose_stamped(nav,1.6 ,0.0 ,-1.5 )
	point3 = create_pose_stamped(nav,-2.0 ,-4.0 ,1.5 )
	
	waypoints = [point1, point2, point3]
	nav.followWaypoints(waypoints)
	
	while not nav.isTaskComplete():
		feedback = nav.getFeedback()
		print(feedback)
	
	print(nav.getResult(), " Done with waypoints, shutting down")
	
	
	rclpy.shutdown()
	
if __name__ == '__main__':
	main()
	

