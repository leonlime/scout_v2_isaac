import os
from launch_ros.actions import Node
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    scout_v2_ros2_path = get_package_share_directory('scout_v2_ros2')
    rviz_config_file = os.path.join(scout_v2_ros2_path,
                                    'config/rviz',
                                    'config.rviz')
    print(scout_v2_ros2_path)
    print(rviz_config_file)

    return LaunchDescription([    
        Node(package="rviz2",
             executable="rviz2",
             name='rviz2',
             arguments=['-d', rviz_config_file])
    ])
    