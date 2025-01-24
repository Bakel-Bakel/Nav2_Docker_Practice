#!/bin/bash

set -e

source /opt/ros/humble/setup.bash
source /app/ws/install/setup.bash

exec "$@"
