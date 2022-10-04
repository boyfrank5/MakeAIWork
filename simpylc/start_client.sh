#!/usr/bin/env bash

export LIBGL_ALLOW_SOFTWARE=1

(cd simulations/car/control_client; python ./drivingAgent.py) 

# (cd simulations/car/control_client; python ./hardcoded_client.py) > log.txt


