# scout_v2_isaac
## Overview
![readme_top](/pictures/readme_top.png)

- Agilex Scout v2.0 simulation for NVIDIA Isaac Sim.

**Keywords:** simulation, Isaac, scout, agilex

### Demonstration
<iframe width="560" height="315" src="https://www.youtube.com/embed/7o9y21d7H-U?si=F3a-gxTb6RUHaioJ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## License

- The source code is released under a [MIT License](LICENSE).

**Author:** 
Leonardo Lima (leo.mendes21@hotmail.com)

## Instalation
To utilize this package, simply clone the repository and install all necessary dependencies.

## Dependencies
The `scout_v2_isaac` package has been created and tested under Ubuntu 22.04. This is research code, expect that it changes often and any fitness for a particular purpose is disclaimed.

| OS | Isaac Sim | ROS 2 |
| :---: | :---: | :---: |
| [Ubuntu 22.04](https://releases.ubuntu.com/jammy/) | [2022.2.1](https://developer.nvidia.com/isaac/sim) | [Humble](https://docs.ros.org/en/humble/Installation.html) |

## How to use 
### Simulation setup
First, you need to open the terminal and create a ROS2 workspace
```
mkdir -p scout_ws/src
```
go to the src folder and clone the repository
```
cd scout_ws/src
git clone https://github.com/leonlime/scout_v2_isaac.git
```

build the package
```
cd ..
source /opt/ros/humble/setup.bash
colcon build
```
### Running the simulation
Open the terminal, navigate to the workspace you created before and source ROS2. Don’t forget, **always before opening Isaac Sim**, the first thing to do is start a terminal and source ROS2 Humble.
```
cd scout_ws
source /opt/ros/humble/setup.bash
```
Open `Isaac sim`, inside Isaac sim, change the extension `ROS BRIDGE` to `ROS2 HUMBLE BRIDGE`. Open `scout_v2_simulation.usd` file and click in Isaac Play button.

Go back to the terminal and check the ROS2 topics
```
ros2 topic list
```
To visualize the camera images, LiDAR and odometry, open Rviz
```
ros2 launch scout_v2_ros2 scout_v2_rviz.launch.py
```
You can navigate using teleop twist command
```
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

#### PS: If this simulation is too heavy for your PC. You can try disable left and right camera plugin.
