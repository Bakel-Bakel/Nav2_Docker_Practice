FROM osrf/ros:humble-desktop

SHELL ["/bin/bash","-c"]

WORKDIR /app

COPY src ws/src

RUN cd ws && \
    source /opt/ros/humble/setup.bash && \
    colcon build

COPY entrypoint.sh /

ENTRYPOINT [ "/entrypoint.sh" ]

CMD ["bash"]