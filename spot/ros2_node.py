import rclpy
from rclpy.node import Node

class SpotNode(Node):
    def __init__(self):
        super().__init__('spot_node')
        self.get_logger().info('Spot ROS2 node initialized')
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info('Spot node running...')

def main(args=None):
    rclpy.init(args=args)
    node = SpotNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
