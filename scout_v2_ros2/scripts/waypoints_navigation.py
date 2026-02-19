import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from geometry_msgs.msg import PoseStamped
from nav2_msgs.action import NavigateToPose
import math


class Waypoints_navigator(Node):
    def __init__(self):
        super().__init__('nav_client')
        self.client = ActionClient(self, NavigateToPose, '/navigate_to_pose')
        self.waypoints = []
        self.get_logger().info('Node started, starting navigation...')

    def quaternion_from_yaw(self, yaw):
        return (0.0, 0.0, math.sin(yaw/2), math.cos(yaw/2))

    def add_waypoint(self, list):
        self.waypoints.append(list)

    def go_to(self, x, y, yaw_deg):
        self.client.wait_for_server()
        yaw = math.radians(yaw_deg)

        qx, qy, qz, qw = self.quaternion_from_yaw(yaw)

        goal = NavigateToPose.Goal()
        goal.pose = PoseStamped()
        goal.pose.header.frame_id = 'map'
        goal.pose.pose.position.x = x
        goal.pose.pose.position.y = y
        goal.pose.pose.orientation.z = qz
        goal.pose.pose.orientation.w = qw

        future = self.client.send_goal_async(goal)
        rclpy.spin_until_future_complete(self, future)
        goal_handle = future.result()

        result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, result_future)

    def nav_into_points(self):
        for i in range(len(self.waypoints)):
            self.go_to(float(self.waypoints[i][0]),
                       float(self.waypoints[i][1]),
                       float(self.waypoints[i][2]))
            self.get_logger().info(f"Point {i+1}/{len(self.waypoints)} reached!")
        self.get_logger().info('All points reached!!')

def main():
    rclpy.init()
    nav = Waypoints_navigator()

    nav.add_waypoint([0, 0, 0])
    nav.add_waypoint([10, 0, 0])
    nav.add_waypoint([5, 0, 0])
    nav.add_waypoint([5, 7, 0])
    nav.add_waypoint([3, -10, 0])

    nav.nav_into_points()

    nav.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
