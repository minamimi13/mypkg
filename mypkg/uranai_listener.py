# SPDX-FileCopyrightText: 2023 Saori Kitami　　　　　
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(msg):
    global node

    message = [
        "今日の運勢は希望が実現するでしょう\n", 
        "今日の運勢は目上からの強要が激しいでしょう\n", 
        "今日の運勢は事態が好転するでしょう\n", 
        "今日の運勢は気まぐれと浮気心に注意しましょう\n", 
        "今日の運勢は過激な闘争心が湧くでしょう\n", 
        "今日の運勢は情熱と熱意が湧くでしょう\n", 
        "今日の運勢は難問の発生に気をつけましょう\n",  
        "今日の運勢は豊かな成果があります\n", 
        "今日の運勢は行動力の勝利です\n", 
        "今日の運勢は決断と実行が発揮されるでしょう\n", 
        "今日の運勢はやる気と向上心があがります\n", 
        "今日の運勢は健康に注意してください\n", 
        "今日の運勢は大きな変化があります\n", 
        "今日の運勢は失望と落胆です\n", 
        "今日の運勢は陽気な一日になるでしょう\n", 
        "今日の運勢は異性関係不調です\n", 
        "今日の運勢は磁力的な魅力が湧き出るでしょう\n", 
        "今日の運勢は衝動による失敗をしてしまうでしょう\n", 
        "今日の運勢は突然の損失があるでしょう\n", 
        "今日の運勢は重要な出会いがあります\n", 
        "今日の運勢は名誉と表彰に見回られるでしょう\n"
    ]

    node.get_logger().info(message[msg.data])

rclpy.init()
node = Node("uranai_listener")
pub = node.create_subscription(Int16, "uranai", cb, 10)

rclpy.spin(node)
