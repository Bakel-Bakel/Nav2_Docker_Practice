from std_msgs.msg import String
import rclpy
from rclpy.node import Node

topicName = 'Test_ROSpy_Communication'

class SubscriberNode(Node):

    def __init__(self):
        super().__init__("subscriber_node")
        self.subcriberCreated = self.create_subscription(String, topicName, self.callBackFunctionSubscriber, 20)
        self.subcriberCreated

    def callBackFunctionSubscriber(self, receivedMessage):
        self.get_logger().info("Copy! %s" %receivedMessage.data)

def main(args=None):

    rclpy.init(args=args)
    subscriberNode = SubscriberNode()
    rclpy.spin(subscriberNode)

    subscriberNode.destroy_node()
    rclpy.shutdown()

if __name__== '__main__':
    main()