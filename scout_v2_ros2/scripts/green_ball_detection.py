import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from controller import Velocity_controller
from geometry_msgs.msg import Twist


class green_ball_tracker(Node):
    def __init__(self):
        super().__init__('green_ball_tracker')
        self.create_subscription(Image,'/scoutv2/camera', self.callback, 10)
        self.bridge = CvBridge()

        self.linear_vel_control = Velocity_controller(1, -1, 0.01, 0, 0)
        self.angular_vel_control = Velocity_controller(1, -1, 0.01, 0, 0)
        self.velocity_pub = self.create_publisher(Twist, '/cmd_vel', 10)

        self.get_logger().info('Searching for a green ball...')

    def green_ball_detection(self, image):
        cv2_frame = self.bridge.imgmsg_to_cv2(image, "bgr8")
        hsv_frame = cv2.cvtColor(cv2_frame, cv2.COLOR_BGR2HSV)

        green_lower = (35, 100, 100)
        green_upper = (85, 255, 255)
        mask_green = cv2.inRange(hsv_frame, green_lower, green_upper)
        mask_green = cv2.erode(mask_green, None, iterations=2)
        mask_green = cv2.dilate(mask_green, None, iterations=2)
        cnt_green = cv2.findContours(mask_green.copy(),
                                      cv2.RETR_EXTERNAL,
                                      cv2.CHAIN_APPROX_SIMPLE)[-2]

        contours_poly = []
        centers = []
        radius = []

        for index, obj_cnt in enumerate(cnt_green):
            contours_poly.append(cv2.approxPolyDP(obj_cnt,
                                                  0.009 * cv2.arcLength(obj_cnt, True), True))
            aux1, aux2 = cv2.minEnclosingCircle(contours_poly[index])
            centers.append(aux1)
            radius.append(aux2)

        if not contours_poly:
            return (None, None)

        return (centers[0][0], radius[0])

    def cmd_vel_pub(self, linear, angular):
        msg = Twist()
        msg.linear.x = float(linear)
        msg.angular.z = float(angular)
        self.velocity_pub.publish(msg)
        self.get_logger().info('Publishing velocity')

    def callback(self, data):
        center, radius = self.green_ball_detection(data)

        if center is not None:
            linear_vel = self.linear_vel_control.calculate(1, 180, radius)
            angular_vel = self.angular_vel_control.calculate(1, 645, center)

            self.cmd_vel_pub(linear_vel, angular_vel)

        else:
            self.cmd_vel_pub(0, 0)

def main():
    rclpy.init()
    node = green_ball_tracker()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
