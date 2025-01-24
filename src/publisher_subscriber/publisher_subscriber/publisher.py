from std_msgs.msg import String

import rclpy
from rclpy.node import Node

topicName = 'Test_ROSpy_Communication'


class PublisherNode(Node):

    def __init__ (self):

        super().__init__('publisher_node')

        self.publisherCreated = self.create_publisher (String, topicName, 20)
        self.counter = 0
        communicationPeriod = 1
        self.period = self.create_timer(communicationPeriod, self.callBackFunctionPublisher)

    def callBackFunctionPublisher(self):
        messageToBeSent = String()
        messagePythonString = "This is Bakel testing ROSpy %d" %self.counter
        messageToBeSent.data = messagePythonString

        self.publisherCreated.publish(messageToBeSent)
        self.counter += 1
        self.get_logger().info("Published Message: %s" %messageToBeSent)

def main(args=None):
    rclpy.init(args=args)
    publisherNode = PublisherNode()
    
    rclpy.spin(publisherNode)

    publisherNode.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()