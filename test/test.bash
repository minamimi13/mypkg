#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1" # 引数があったら、そちらをホームに変える。

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

# talk_listen_launch.py のテスト
timeout 10 ros2 launch mypkg talk_listen_launch.py > /tmp/mypkg.log

# uranai_talk_listen_launch.py のテスト
timeout 10 ros2 launch mypkg uranai_talk_listen_launch.py > /tmp/uranai_mypkg.log

# どちらかのログに期待する文字列が含まれていれば 0 を返す
if grep -q 'Listen: 10' /tmp/mypkg.log && grep -q '今日の運勢' /tmp/uranai_mypkg.log; then
    echo 0
else
    echo 1
fi
