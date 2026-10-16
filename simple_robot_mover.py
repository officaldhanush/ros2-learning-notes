import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class SimpleRobotMover(Node):
    def __init__(self):
        super().__init__('simple_robot_mover')
        
        # Create a publisher to send movement commands to the robot's topic (/cmd_vel)
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        
        # Set a timer to run the command every 1 second
        timer_period = 1.0 
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('Robot Mover Node has started successfully!')

    def timer_callback(self):
        # Create a Twist message (used for velocity in ROS 2)
        msg = Twist()
        
        # Make the robot move forward slowly
        msg.linear.x = 0.2  # Moving forward speed (meters/second)
        msg.angular.z = 0.0 # No turning (rotation speed)
        
        # Publish the message
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing command: Moving forward at 0.2 m/s')

def main(args=None):
    rclpy.init(args=args)
    simple_robot_mover = SimpleRobotMover()
    
    try:
        rclpy.spin(simple_robot_mover)
    except KeyboardInterrupt:
        pass
    
    # Clean up and shutdown when done
    simple_robot_mover.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
