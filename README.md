# scout_v2_isaac
## Overview
![readme_top](/pictures/readme_top.png)

- Agilex Scout v2.0 simulation for NVIDIA Isaac Sim.

**Keywords:** simulation, Isaac, scout, agilex

## License

- The source code is released under a [MIT License](LICENSE).

**Author:** 
Leonardo Lima (leo.mendes21@hotmail.com)

## Prerequisites
The `scout_v2_isaac` package has been created and tested under Ubuntu 22.04. This is research code, expect that it changes often and any fitness for a particular purpose is disclaimed.

| OS | Isaac Sim | ROS 2 |
| :---: | :---: | :---: |
| [Ubuntu 22.04](https://releases.ubuntu.com/jammy/) | [5.1.0](https://docs.isaacsim.omniverse.nvidia.com/5.1.0/overview/release_notes.html) | [Humble](https://docs.ros.org/en/humble/Installation.html) |

Install `navigation2` and `slam-toolbox` packages:
```bash
sudo apt update
sudo apt install ros-humble-slam-toolbox
sudo apt install ros-humble-navigation2 ros-humble-nav2-bringup
```

## How to use 
### Simulation setup
Clone and build the repository inside a ROS 2 workspace:
```bash
mkdir -p scout_ws/src
```
Clone the repository:
```bash
cd ~/scout_ws/src
git clone https://github.com/leonlime/scout_v2_isaac.git
```
Navigate to workspace root and install dependencies:
```bash
cd ~/scout_ws
rosdep update
rosdep install --from-paths src --ignore-src -r -y
```

Build the workspace:
```bash
source /opt/ros/humble/setup.bash
colcon build
```

### Running the simulation
Open the terminal, navigate to the workspace you created before and source ROS2:
```bash
cd ~/scout_ws
source /opt/ros/humble/setup.bash
source install/setup.bash
```
#### Launching Simulation
1. Open **Isaac Sim 5.1**.
2. Inside Isaac Sim, open the warehouse scene:
   * Go to **File** > **Open**
   * Navigate to the USD file inside the package:
     ```text
     scout_v2_isaac/isaac_models/warehouse_w_robot.usd
     ```
   * Click on **Play** button on the left menu and go back to the terminal.

#### Check the ROS 2 topics
```bash
ros2 topic list
```
#### Visualize camera, map and navigation on Rviz
```bash
ros2 launch scout_v2_ros2 scout_v2_rviz.launch.py
```
### Mapping and Navigation
#### Start slam toolbox for mapping
```bash
ros2 launch scout_v2_ros2 slam_toolbox_online_async.launch.py
```
#### Start navigation
```bash
ros2 launch scout_v2_ros2 navigation.launch.py
```
### Navigate using teleop 
#### Keyboard teleop
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
#### Joystick teleop
```bash
ros2 launch teleop_twist_joy teleop-launch.py
```
### Autonomous Navigation
#### Waypoints navigation
```bash
ros2 run scout_v2_ros2 waypoints_navigation
```
#### Follow the green ball
```bash
ros2 run scout_v2_ros2 green_ball_detection
```

## Bugs & Feature Requests
Please report bugs and request features using the [Issue Tracker](https://github.com/leonlime/scout_v2_isaac/issues).
