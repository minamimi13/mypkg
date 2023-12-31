# SPDX-FileCopyrightText: 2023 Saori Kitami 　　　　　
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    uranai_talker = launch_ros.actions.Node(
            package='mypkg',
            executable='uranai_talker',
            )
    uranai_listener = launch_ros.actions.Node(
            package='mypkg',
            executable='uranai_listener',
            output='screen'
            )

    return launch.LaunchDescription([uranai_talker, uranai_listener])
