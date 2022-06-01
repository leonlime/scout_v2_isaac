import os
from launch_ros.actions import Node
from launch import LaunchDescription


def generate_launch_description():
    scout_v2_ros2_path = get_package_share_directory('scout_v2_ros2')
    rviz_config_file = os.path.join(scout_v2_ros2_path,
                                    'config/rviz',
                                    'config.rviz')

    return LaunchDescription([    
        Node(package="rviz2",
             executable="rviz2",
             name='rviz2',
             arguments=['-d', rviz_config_file])
    ])