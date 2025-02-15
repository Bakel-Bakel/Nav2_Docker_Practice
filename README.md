<!-- GETTING STARTED -->
## Overview
- This project is being created by Bakel Bakel under the supervision of Mr. Stefano (PhD in view). The package builds on the initial dockerfile used for the rover for autonomous navigation at PrismaLab.

- Basically, the dockerfile used here has been modified to suit this particular project. It still retains the main features of the initial rover dockerfile, just [Little Adjustments](#little-adjustments) to meet the need of this project. 
  

## Table of Contents

1. [How to set up](#How-to-set-up)
2. [Packages used in Dockerfile](#Packages-used-in-Dockerfile)
3. [Little Adjustments](#Little-Adjustments)

## How to run
Firstly, get docker installed and fully running. [How to install docker](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)

1. Now to build the dockerfile into an image, Open a terminal in the repo and source the build file. 
Run:

```sh
source docker_build.sh <IMAGE_NAME>
```
where <IMAGE_NAME> is a name for the image you want to build.

2. To run the built docker image as a container, In the terminal in the repo, source the run file. Run:

 
```sh
source docker_run.sh <IMAGE_NAME> <CONTAINER_NAME>
```
where <IMAGE_NAME> is the name of the image you have just built, while <CONTAINER_NAME> is a name for the container hosting the image.

3. If you want to attach additional terminals to the container you need to keep it running (docker_run.sh script). You can attach a new terminal by running the following command

```sh
docker exec -it $(docker ps -aqf "name=<CONTAINER_NAME>") bash
```
Note: The container's root password is "user" by default.

4. Launch the turtle robot in gazebo

```sh
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

5. Launch the turtle robot in rviz for nav2
```sh
ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True map:=maps/turtle_world/my_maps.yaml
```

6. Launch and display the custom robot in rviz
```sh
ros2 launch urdf_tutorial display.launch.py model:=/home/user/ros2_ws/src/my_robot.urdf
```
7. Start a Navigation launch file
```sh
ros2 launch nav2_bringup navigation_launch.py
(add use_sim_time:=True if using Gazebo)
```
8. Start SLAM with slam_toolbox
```sh
ros2 launch slam_toolbox online_async_launch.py use_sim_time:=True
```

9. Start Rviz
```sh
ros2 run rviz2 rviz2
```
Note you will need to configure riz2 after starting by adding the maps, tf, laserscan and other parameters.

10. Things to do: Next I will learn how to directly interact with the Nav2 interface with my code, for example using the Simple Commander API

## Packages used in Dockerfile
- kmod
- minicom
- screen
- xacro
- rviz2
- librealsense2
- realsense2
- navigation2
- nav2-bringup
- slam-toolbox
- rmw-cyclonedds-cpp
- joint-state-publisher-gui
External repositories included in this porject:
- [TEB Local Planner](https://github.com/rst-tu-dortmund/teb_local_planner/tree/ros2-master)
- [Aruco Marker Pose Estimation](https://github.com/AIRLab-POLIMI/ros2-aruco-pose-estimation)
- [Costmap Converter](https://github.com/rst-tu-dortmund/costmap_converter/tree/ros2/)


## Little Adjustments

The following were added to the dockerfile to ensure it had what I needed for practice.

```sh
RUN apt install ros-humble-turtlebot3-teleop -y
RUN apt install ros-humble-turtlebot3-cartographer -y
RUN apt install ros-humble-turtlebot3-navigation2 -y
RUN apt install ros-humble-urdf-tutorial -y
RUN apt install gedit -y

RUN sudo sed -i 's/^\(\s*robot_model_type:\s*\).*/\1"nav2_amcl::DifferentialMotionModel"/' /opt/ros/humble/share/turtlebot3_navigation2/param/waffle.yaml

COPY --chown=user ./maps ${HOME}/ros2_ws/maps
COPY --chown=user ./worlds ${HOME}/ros2_ws/worlds

RUN echo "export TURTLEBOT3_MODEL=waffle" >>  ${HOME}/.bashrc
RUN echo "export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp" >>  ${HOME}/.bashrc
```
   
   
   
   
   
   
   
   
   
   
   
   
   

