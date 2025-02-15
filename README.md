<!-- GETTING STARTED -->
## Overview
- This project is being created by Bakel Bakel under the supervision of Mr. Stefano (PhD in view). The package builds on the initial dockerfile used for the rover for autonomous navigation at PrismaLab. This package is a ros2 porting of a indoor navigation project and implement integration with Slam and Navigation ROS2 package.

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
   
   
   
   
   
   
   
   
   
   
   
   
   
   

