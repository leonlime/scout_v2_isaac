cmake_minimum_required(VERSION 3.8)
project(scout_v2_ros2)
find_package(ament_cmake REQUIRED)
install(DIRECTORY launch config maps scripts
  DESTINATION share/${PROJECT_NAME}
)
ament_package()
``