#!/user/bin/python3
# SPDX-FileCopyrightText: 2023 Saori Kitami　　　　　
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import random

class UranaiTalker():
    def __init__(self, node):
        self.pub = node.create_publisher(Int16, "uranai", 10)
        self.n = randomInt()
        node.create_timer(0.5, self.cb)

    def cb(self):
        msg = Int16()
        msg.data = self.n
        self.pub.publish(msg)
        self.n = randomInt()

def randomInt():
    return random.randint(0, 20)

def main():
    rclpy.init()
    node = Node("uranai_talker")
    talker = UranaiTalker(node)
    rclpy.spin(node)

if __name__ == '__main__':
    main()
