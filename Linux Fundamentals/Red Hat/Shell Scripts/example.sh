#!/bin/bash
# Script to let users perform yum checks
# Usage: ./web_admin.sh <action> <package>
# check-updates: No package to specify

# Script Inputs
ARG1=$1
ARG2=$2

# Other Variables
YUM=/usr/bin/yum

if [ "$ARG1" = "check-updates" ] ; then
        $YUM check-update >> web_admin.log
        YUM_RESULT=$?
                case $YUM_RESULT in
                        100)
                                echo "Updates available!"
                                exit 111