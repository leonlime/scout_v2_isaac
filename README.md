# scout_v2_isaac
Isaac Sim simulation for Agilex Scout v2.0

- 11/04/2023 Updated to run in Isaac 2022.2.1 and ROS Humble.

## How to test this simulation

1. Open a terminal and source ROS Humble:
    - $ source /opt/ros/humble/setup.bash
2. Open Isaac sim 
3. Inside Isaac sim, change the extension "ROS BRIDGE" to "ROS2 HUMBLE BRIDGE"
4. Open "scout_v2_simulation.usd" file
5. Click in Issac Play button, back to the first terminal and type (to check if connection is ok):
    - $ ros2 topic list

### To open rviz2 you can use this launch:
- ros2 launch sout_v2_ros scout_v2_rviz.launch.py


PS: If this simulation is too heavy for your PC. You can try disable left and right camera plugin.