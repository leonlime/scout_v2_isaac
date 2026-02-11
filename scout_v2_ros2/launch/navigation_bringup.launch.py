from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_share = get_package_share_directory('scout_v2_ros2')
    default_params = os.path.join(pkg_share, 'config', 'nav2_params.yaml')

    params_arg = DeclareLaunchArgument(
        'params_file', default_value=default_params,
        description='Arquivo de parâmetros do Nav2 (odom-only)'
    )
    use_sim_time_arg = DeclareLaunchArgument(
        'use_sim_time', default_value='true',
        description='Usar sim time'
    )

    # Nós principais do Nav2 (sem map_server e sem amcl)
    controller_server = Node(
        package='nav2_controller',
        executable='controller_server',
        output='screen',
        parameters=[LaunchConfiguration('params_file')]
    )
    planner_server = Node(
        package='nav2_planner',
        executable='planner_server',
        output='screen',
        parameters=[LaunchConfiguration('params_file')]
    )
    bt_navigator = Node(
        package='nav2_bt_navigator',
        executable='bt_navigator',
        output='screen',
        parameters=[LaunchConfiguration('params_file')]
    )
    behavior_server = Node(
        package='nav2_behaviors',
        executable='behavior_server',
        name='behavior_server',
        output='screen',
        parameters=[LaunchConfiguration('params_file')]
    )
    waypoint_follower = Node(
        package='nav2_waypoint_follower',
        executable='waypoint_follower',
        name='waypoint_follower',
        output='screen',
        parameters=[LaunchConfiguration('params_file')]
    )

    lifecycle_manager = Node(
        package='nav2_lifecycle_manager',
        executable='lifecycle_manager',
        name='lifecycle_manager_navigation',
        output='screen',
        parameters=[{
            'use_sim_time': LaunchConfiguration('use_sim_time'),
            'autostart': True,
            'node_names': [
                'controller_server',
                'planner_server',
                'bt_navigator',
                'behavior_server',
                'waypoint_follower'
            ]
        }]
    )

    # (Opcional) RViz já com Nav2; ajuste Fixed Frame para 'odom' manualmente
    rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'
    )

    return LaunchDescription([
        params_arg,
        use_sim_time_arg,
        controller_server,
        planner_server,
        bt_navigator,
        behavior_server,
        waypoint_follower,
        lifecycle_manager,
        rviz
    ])